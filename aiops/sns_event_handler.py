import json


def process_sns_event(event):
    print("=== AIOps Event Received ===")

    message = event.get("Message", "")

    try:
        alarm = json.loads(message)
    except json.JSONDecodeError:
        alarm = {
            "raw_message": message
        }

    incident = {
        "source": "CloudWatch",
        "event_type": "alarm",
        "alarm": alarm,
        "status": "OPEN"
    }

    with open("incident.json", "w") as file:
        json.dump(incident, file, indent=2)

    print("Incident created: incident.json")


if __name__ == "__main__":

    test_event = {
        "Message": json.dumps({
            "AlarmName": "AIOps-Linux-High-Memory",
            "NewStateValue": "ALARM",
            "NewStateReason": "Memory usage exceeded 70%",
            "MetricName": "mem_used_percent",
            "Threshold": 70,
            "InstanceId": "i-0b79fde958892b276"
        })
    }

    process_sns_event(test_event)
