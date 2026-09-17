import os
import json
import requests

routing_key = os.environ["PAGERDUTY_ROUTING_KEY"]

with open("incident.json", "r") as file:
    incident = json.load(file)

alarm = incident.get("alarm", {})

metric = alarm.get("MetricName", "Unknown")
instance = alarm.get("InstanceId", "Unknown")
alarm_name = alarm.get("AlarmName", "Unknown Alarm")
reason = alarm.get("NewStateReason", "Unknown reason")

payload = {
    "routing_key": routing_key,
    "event_action": "trigger",
    "payload": {
        "summary": f"AIOps Alert: {metric} exceeded threshold",
        "severity": "critical",
        "source": instance,
        "timestamp": alarm.get("Timestamp"),
        "component": "rehabilitation-yoga",
        "class": "High Memory",
        "custom_details": {
            "alarm": alarm_name,
            "metric": metric,
            "instance": instance,
            "reason": reason,
            "status": incident.get("status"),
            "source": incident.get("source")
        }
    }
}

response = requests.post(
    "https://events.pagerduty.com/v2/enqueue",
    json=payload,
    timeout=10
)

print("PagerDuty HTTP status:", response.status_code)
print("PagerDuty response:", response.text)
