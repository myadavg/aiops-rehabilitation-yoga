import boto3
import json
from datetime import datetime, timedelta, timezone

REGION = "eu-west-2"
INSTANCE_ID = "i-0b79fde958892b276"
THRESHOLD = 70

cloudwatch = boto3.client("cloudwatch", region_name=REGION)

end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(hours=1)

response = cloudwatch.get_metric_statistics(
    Namespace="CWAgent",
    MetricName="mem_used_percent",
    Dimensions=[
        {"Name": "InstanceId", "Value": INSTANCE_ID},
        {"Name": "ImageId", "Value": "ami-0224ce6f9504665ee"},
        {"Name": "InstanceType", "Value": "t3.micro"},
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=300,
    Statistics=["Average"],
)

datapoints = sorted(
    response["Datapoints"],
    key=lambda x: x["Timestamp"]
)

for point in datapoints:
    value = point["Average"]
    timestamp = point["Timestamp"]

    if value > THRESHOLD:
        print(f"[ALERT] {timestamp} - Memory usage: {value:.2f}%")

        incident = {
            "source": "CloudWatch",
            "service": "rehabilitation-yoga",
            "instance": INSTANCE_ID,
            "metric": "mem_used_percent",
            "value": round(value, 2),
            "threshold": THRESHOLD,
            "severity": "HIGH",
            "timestamp": timestamp.isoformat()
        }

        with open("incident.json", "w") as file:
            json.dump(incident, file, indent=2)

    else:
        print(f"[OK] {timestamp} - Memory usage: {value:.2f}%")
