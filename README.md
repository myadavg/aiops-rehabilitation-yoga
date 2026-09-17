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
