# 🤖 AI-Powered DevOps & AIOps Incident Management Platform

An end-to-end DevOps, Observability, AIOps and Generative AI project that demonstrates how infrastructure incidents can be detected, analysed using AI, sent to an incident-management platform, automatically remediated, and verified for recovery.

This project combines AWS, Kubernetes, Docker, Jenkins, CloudWatch, Elastic/Kibana, AppDynamics, RAG, ChromaDB, Groq LLM, PagerDuty and Python automation into a single incident-management workflow.

## 📌 Project Overview

The application is a containerized rehabilitation/yoga website deployed on Kubernetes running on AWS.

The platform monitors the infrastructure and application environment using multiple observability tools.

When a high-memory condition is detected, the AIOps workflow processes the incident and performs automated analysis and remediation.

### End-to-End Workflow

```text
AWS CloudWatch
      ↓
CloudWatch Alarm
      ↓
SNS
      ↓
AIOps Event Handler
      ↓
RAG + ChromaDB
      ↓
AI Agent + Groq LLM
      ↓
Incident RCA
      ↓
PagerDuty
      ↓
Kubernetes Remediation
      ↓
Recovery Verification

# 🛠️ Technology Stack

## Cloud & Infrastructure

- AWS EC2
- AWS ECR
- AWS S3
- AWS Elastic Load Balancer
- AWS CloudWatch
- AWS SNS
- AWS IAM

## DevOps

- Git
- GitHub
- Jenkins
- Docker
- Kubernetes
- kOps
- Terraform
- Linux

## Observability

- AWS CloudWatch
- Elastic Cloud
- Kibana
- Elastic Agent
- AppDynamics

## AI / AIOps

- Python
- Groq LLM
- AI Agent
- RAG
- ChromaDB
- Large Language Models

## Incident Management

- PagerDuty
- PagerDuty Events API v2
- Automated Kubernetes remediation
- Recovery verification

# 🌐 Application

The project uses a rehabilitation/yoga website as the application being monitored.

The website is packaged into a Docker container using Nginx and deployed to Kubernetes.

### Application Flow

```text
Website Source Code
        ↓
      Docker
        ↓
      Nginx
        ↓
 Kubernetes Pod
        ↓
 LoadBalancer
        ↓
    Website

The application is stored in GitHub, built through Jenkins, packaged as a Docker image, pushed to Amazon ECR, and deployed to Kubernetes.

Application Components
HTML
CSS
JavaScript
Nginx
Docker
Kubernetes
AWS Load Balancer

# 🔄 CI/CD Implementation

I implemented a Jenkins CI/CD pipeline to automate the application container build and publishing process.

### Pipeline

GitHub → Jenkins → Docker Build → Docker Test → Amazon ECR

The Jenkins pipeline:

- Checks out the application source code from GitHub
- Builds the Docker image
- Tests the container
- Authenticates with Amazon ECR
- Pushes the application image to ECR

---

# ☸️ Kubernetes Deployment

I created a Kubernetes cluster on AWS EC2 using kOps and deployed the rehabilitation/yoga application.

### Deployment Flow

GitHub
↓
Docker
↓
Amazon ECR
↓
Kubernetes
↓
Application Pod
↓
AWS Load Balancer
↓
Website

The application is exposed through a Kubernetes LoadBalancer service and is accessible through the AWS load balancer endpoint.

---

# 📊 Observability

I implemented multiple monitoring and observability solutions for the Kubernetes environment.

### AWS CloudWatch

I configured the CloudWatch Agent to collect Linux system metrics.

The main metric used for the AIOps workflow is:

`CWAgent / mem_used_percent`

I created the following CloudWatch alarm:

- Alarm: `AIOps-Linux-High-Memory`
- Threshold: 70%
- Evaluation: 2 consecutive 5-minute periods

### Elastic Cloud / Kibana

I deployed Elastic Agent into Kubernetes and connected it to Elastic Cloud.

Kibana is used to investigate:

- Kubernetes logs
- Container logs
- Kubernetes events
- Pod metrics
- Node metrics

### AppDynamics

I deployed the AppDynamics Cluster Agent into Kubernetes and connected it to the AppDynamics SaaS controller for Kubernetes observability.

---

# 🤖 AIOps Implementation

I built a Python-based AIOps workflow that processes infrastructure incidents and performs AI-assisted incident analysis.

### Workflow

CloudWatch
↓
Alarm
↓
SNS Event
↓
Incident JSON
↓
RAG / ChromaDB
↓
Groq LLM
↓
AI RCA
↓
PagerDuty
↓
Kubernetes Remediation
↓
Recovery Verification

---

# 🧠 RAG + AI Incident RCA

I created an operational knowledge base containing troubleshooting information for high-memory incidents.

The knowledge is stored and retrieved using ChromaDB.

When an incident is processed:

1. The incident information is loaded.
2. Relevant troubleshooting knowledge is retrieved from ChromaDB.
3. The incident and retrieved knowledge are sent to the Groq LLM.
4. The LLM generates an operational RCA.

The RCA contains:

- Incident summary
- Possible root cause
- Severity
- Recommended remediation
- Verification steps

The workflow separates observed incident information from possible causes so that a hypothesis is not automatically treated as a confirmed root cause.

---

# 🚨 PagerDuty Integration

I integrated the AIOps workflow with PagerDuty using the PagerDuty Events API v2.

The workflow sends the incident details and AI-generated RCA to PagerDuty.

### Flow

AIOps Workflow
↓
PagerDuty Events API
↓
PagerDuty Incident

This allows the detected incident and its analysis to be available in the incident-management platform.

---
# 🔧 Automated Kubernetes Remediation

I implemented a Python remediation script to restart the affected Kubernetes deployment.

The remediation workflow:

1. Checks Kubernetes API availability.
2. Restarts the application deployment.
3. Waits for the workload to recover.
4. Checks pod status.
5. Checks container readiness.

Example command:

```bash
kubectl rollout restart deployment/rehabilitation-yoga

Recovery is verified when the application pod reaches:

Status: Running
Ready: true

If the Kubernetes API is temporarily unavailable during verification, the workflow reports that verification is pending instead of incorrectly reporting a successful recovery.

📁 Project Structure
aiops/
├── rag/
│   ├── knowledge.txt
│   ├── build_knowledge_base.py
│   └── chroma_db/
│
├── pagerduty/
│   └── send_incident.py
│
├── remediation/
│   └── kubernetes_remediation.py
│
├── cloudwatch_collector.py
├── sns_event_handler.py
├── rca_agent.py
├── aiops_workflow.py
└── incident.json


✅ What I Implemented
AWS EC2 infrastructure
Dockerized rehabilitation/yoga application
GitHub source control
Jenkins CI/CD pipeline
Amazon ECR container registry
Kubernetes cluster using kOps
Kubernetes application deployment
AWS Load Balancer
CloudWatch monitoring
CloudWatch memory alarm
SNS event layer
Elastic Cloud / Kibana observability
AppDynamics Cluster Agent
Python-based AIOps workflow
RAG knowledge base
ChromaDB
Groq LLM integration
AI-assisted incident RCA
PagerDuty Events API integration
Automated Kubernetes remediation
Kubernetes recovery verification
🚀 Future Enhancements
Add CPU, disk and pod-failure incident scenarios
Expand the RAG knowledge base
Add application health checks
Add automated deployment rollback
Add additional remediation actions
Build an AIOps dashboard
Connect the event-processing layer directly to AWS services for a fully automated production-style workflow
👩‍💻 Author

Manisha Yadav G

DevOps Engineer | AWS Cloud | Kubernetes | SRE | AIOps | Generative AI


