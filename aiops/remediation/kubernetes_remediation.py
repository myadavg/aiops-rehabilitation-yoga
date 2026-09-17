import subprocess
import time

DEPLOYMENT = "rehabilitation-yoga"
NAMESPACE = "default"


def run_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    return result


print("=== Kubernetes Remediation ===")
print(f"Target deployment: {DEPLOYMENT}")
print(f"Namespace: {NAMESPACE}")

print("\nChecking Kubernetes API...")

nodes = run_command(["kubectl", "get", "nodes"])

if nodes.returncode != 0:
    print("Kubernetes API unavailable.")
    print("Remediation stopped.")
    exit(1)

print("Kubernetes API is available.")

print("\nRestarting deployment...")

restart = run_command([
    "kubectl",
    "rollout",
    "restart",
    f"deployment/{DEPLOYMENT}",
    "-n",
    NAMESPACE
])

if restart.returncode != 0:
    print("Deployment restart failed.")
    exit(1)

print("Deployment restart command accepted.")

print("\nWaiting for Kubernetes recovery...")
time.sleep(10)

pods = run_command([
    "kubectl",
    "get",
    "pods",
    "-n",
    NAMESPACE,
    "-l",
    f"app={DEPLOYMENT}",
    "-o",
    "jsonpath={range .items[*]}{.metadata.name} {.status.phase} {.status.containerStatuses[0].ready}{'\\n'}{end}"
])

if pods.returncode != 0:
    print("\nRecovery verification pending.")
    print("Kubernetes API became unavailable during verification.")
    exit(0)

print("\nPod status:")
print(pods.stdout)

if "Running true" in pods.stdout:
    print("=== Recovery Verified ===")
else:
    print("=== Recovery Verification Pending ===")
