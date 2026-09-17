import json
import chromadb
from groq import Groq

# -----------------------------
# Load incident
# -----------------------------
with open("incident.json", "r") as file:
    incident = json.load(file)

# -----------------------------
# Connect to ChromaDB
# -----------------------------
chroma_client = chromadb.PersistentClient(
    path="./rag/chroma_db"
)

collection = chroma_client.get_collection(
    name="aiops_knowledge"
)

# -----------------------------
# Retrieve relevant knowledge
# -----------------------------
query = f"""
{incident.get('metric', '')}
{incident.get('service', '')}
memory high incident
"""

results = collection.query(
    query_texts=[query],
    n_results=3
)

knowledge = "\n\n".join(results["documents"][0])

# -----------------------------
# Send incident + RAG knowledge
# to Groq
# -----------------------------
client = Groq()

prompt = f"""
You are an AIOps incident analysis agent.

INCIDENT:
{json.dumps(incident, indent=2)}

RETRIEVED KNOWLEDGE FROM RAG:
{knowledge}

Using the incident data and retrieved knowledge, provide:

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

print("\n===== RAG + AI INCIDENT RCA =====\n")
print(response.choices[0].message.content)
