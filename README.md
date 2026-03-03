# 🚀 AI SaaS Idea Validator – Multi-Agent System

## 📌 Project Objective

The AI SaaS Idea Validator is a Multi-Agent AI system designed to evaluate startup ideas by performing:

- Market Research
- Competitor Analysis
- Monetization Planning
- Risk Estimation

The system generates a structured validation report to help founders assess feasibility and make Go / No-Go decisions.

---

## 🏗️ System Architecture

User Input  
↓  
Agent Orchestrator  
↓  
Specialized Agents  
- Market Research Agent  
- Competitor Finder Agent  
- Monetization Analyst Agent  
- Risk Estimator Agent  
↓  
Aggregated Report Generator  
↓  
Streamlit UI Output  

---

## 🤖 Agent Responsibilities

### 1️⃣ Market Research Agent
- Identifies industry trends
- Estimates TAM, SAM, SOM
- Identifies target segments
- Provides growth statistics

### 2️⃣ Competitor Finder Agent
- Identifies direct competitors
- Analyzes pricing models
- Extracts key features
- Generates comparison table

### 3️⃣ Monetization Analyst Agent
- Suggests revenue models
- Estimates pricing tiers
- Suggests upsell strategies
- Provides revenue assumptions

### 4️⃣ Risk Estimator Agent
- Identifies technical risks
- Identifies market risks
- Identifies regulatory risks
- Provides overall risk score

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Modular Agent Architecture
- Pandas
- (Optional Extension: OpenAI / Serper API / Vector DB)

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python -m streamlit run app.py

Then open:
http://localhost:8501