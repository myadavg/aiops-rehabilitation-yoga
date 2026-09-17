import json
import subprocess
import chromadb
from groq import Groq
import requests
import os

# =============================
# 1. Load Incident
# =============================

with open("incident.json", "r") as file:
    incident = json.load(file)

alarm = incident.get("alarm", {})

metric = alarm.get("MetricName", "Unknown")
instance = alarm.get("InstanceId", "Unknown")
alarm_name = alarm.get("AlarmName", "Unknown Alarm")

print("\n=== AIOps Workflow Started ===")
print(f"Alarm: {alarm_name}")
print(f"Metric: {metric}")
print(f"Instance: {instance}")


# =============================
# 2. RAG Retrieval
# =============================

print("\n[1/4] Retrieving knowledge from RAG...")

chroma_client = chromadb.PersistentClient(
    path="./rag/chroma_db"
)

collection = chroma_client.get_collection(
    name="aiops_knowledge"
)

results = collection.query(
    query_texts=[
        f"{metric} high memory Linux incident"
    ],
    n_results=3
)

knowledge = "\n\n".join(results["documents"][0])

print("RAG knowledge retrieved.")


# =============================
# 3. Groq RCA
# =============================

print("\n[2/4] Generating AI RCA...")

client = Groq()

prompt = f"""
You are an AIOps incident analysis agent.

INCIDENT:
{json.dumps(incident, indent=2)}

RETRIEVED RAG KNOWLEDGE:
{knowledge}

Analyze the incident and provide:

1. Incident summary
2. Root cause
3. Severity
4. Recommended remediation
5. Verification steps

Keep the response concise and operational.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "You are an experienced AIOps and SRE incident analyst."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2
)

rca = response.choices[0].message.content

print("\n===== AI RCA =====")
print(rca)


# =============================
# 4. PagerDuty
# =============================

print("\n[3/4] Sending incident to PagerDuty...")

routing_key = os.environ["PAGERDUTY_ROUTING_KEY"]

payload = {
    "routing_key": routing_key,
    "event_action": "trigger",
    "payload": {
        "summary": f"AIOps Alert: {metric} exceeded threshold",
        "severity": "critical",
        "source": instance,
        "component": "rehabilitation-yoga",
        "class": "High Memory",
        "custom_details": {
            "alarm": alarm_name,
            "metric": metric,
            "instance": instance,
            "rca": rca
        }
    }
}

pagerduty_response = requests.post(
    "https://events.pagerduty.com/v2/enqueue",
    json=payload,
    timeout=10
)

print(
    "PagerDuty HTTP status:",
    pagerduty_response.status_code
)


# =============================
# 5. Kubernetes Remediation
# =============================

print("\n[4/4] Starting Kubernetes remediation...")

result = subprocess.run(
    ["python3", "remediation/kubernetes_remediation.py"],
    capture_output=True,
    text=True
)

print(result.stdout)

if result.returncode == 0:
    print("\n=== AIOps Workflow Completed Successfully ===")
    print("Kubernetes remediation and recovery verification succeeded.")
else:
    print("\n=== AIOps Workflow Completed ===")
    print("Kubernetes remediation was attempted, but recovery verification is pending.")
