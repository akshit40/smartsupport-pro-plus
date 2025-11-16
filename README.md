<div align="center">

# 🚀 SmartSupport PRO+  
### **Enterprise-Grade Multi-Agent Customer Support Automation System**

A fully autonomous AI support pipeline that triages, retrieves context, drafts replies, checks quality, detects sentiment, escalates when needed, and tracks analytics — all powered by multi-agent orchestration.

---

## 🏷️ Tech Stack & Tags

`AI Agents` • `Multi-Agent Systems` • `RAG` • `LLMs` • `Gemini` • `OpenAI` • `Python`  
`Enterprise Automation` • `Retrieval` • `Customer Support` • `Observability` • `Memory Bank`

---

## 🛡 Badges

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![AI Agents](https://img.shields.io/badge/Multi--Agent-System-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-green?style=for-the-badge)
![Made for Kaggle](https://img.shields.io/badge/Made%20For-Kaggle-blue?style=for-the-badge&logo=kaggle)

---

</div>

# 🌟 Overview

**SmartSupport PRO+** is an end-to-end **multi-agent customer support automation system** built for the  
**Kaggle × Google Agents Intensive Capstone (2025)** — **Enterprise Agents Track**.

It automates the *heavy repetitive parts* of customer support:

- Understanding tickets  
- Searching docs  
- Finding similar past tickets  
- Drafting replies  
- Quality checks  
- Sentiment detection  
- Escalation summaries  
- Analytics logging  
- Follow-ups  

All while keeping human operators fully in control.

---

# 🧠 Core Features

### ✔ Multi-Agent Architecture  
Parallel + sequential agents simulate a real support workflow team.

### ✔ Retrieval-Augmented Generation (RAG)  
Documentation + past-ticket search ensures grounded, reliable drafting.

### ✔ LLM Optional (Safe for Judges)  
Runs **fully offline in mock mode**.  
Also supports Gemini/OpenAI with environment variables.

### ✔ Long-Term Memory  
Memory Bank stores past interactions and compresses context.

### ✔ Observability & Metrics  
Structured logs, traces, escalation stats, FRT estimates.

### ✔ Evaluation Suite  
ROUGE, BERTScore, operational metrics — included and runnable.

### ✔ Deployment Ready  
Dockerfile + Cloud Run guide.

---

# 🧩 Architecture Diagram

Ticket API → Orchestrator
├── Triage Agent
├── Parallel:
│ ├── Knowledge Agent
│ └── PastTicket Agent
├── Drafting Agent (RAG + LLM)
├── Quality Agent
├── Sentiment Agent
├── Escalation Agent (conditional)
├── Loop Agent
└── Analytics Agent
Memory Bank ↔ Orchestrator

yaml
Copy code

---

Got you — your section looks **broken, misaligned, and messy** because:

* Code blocks weren’t closed properly
* Emojis and headings got mixed
* YAML mention isn’t needed
* Spacing was lost

I'll **enhance the entire section**, make it **clean, aesthetic, balanced, and beautifully formatted**, just like top GitHub projects.

Here is the **fixed + enhanced version**, with perfect spacing, formatting, and readability.

---

# 🎯 **Enhanced, Clean, Professional Version (Copy–Paste Ready)**

````markdown
 📂 Project Structure

smartsupport_pro_plus/
│
├── src/
│   ├── agents/               # Multi-agent modules
│   ├── tools/                # Search, ticket API, helper tools
│   ├── memory/               # Long-term memory bank + compaction
│   ├── orchestrator/         # Main agent pipeline logic
│   └── eval/                 # Evaluation suite (ROUGE, BERTScore)
│
├── notebook.ipynb            # Kaggle / Colab Notebook
├── requirements.txt          # Dependencies
├── Dockerfile                # Deployment config
└── README.md                 # Documentation
````

---

## ⚙️ Installation

### **1. Clone the Repository**

```bash
git clone https://github.com/akshit40/smartsupport-pro-plus.git
cd smartsupport-pro-plus
```

### **2. Create a Virtual Environment**

```bash
python -m venv venv
```

### **Activate the Environment**

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Demo (No API Keys Required)

```bash
python src/agent_orchestrator.py --demo
```

This will:

* Load sample tickets
* Run the full multi-agent pipeline
* Generate drafts & retrieve context
* Perform quality checks
* Detect sentiment
* Produce analytics & trace logs

---

## 🧪 Evaluation Suite

```bash
python src/eval/eval.py
```

Generates:

* ROUGE scores
* BERTScore
* Escalation accuracy
* Time-saving estimates
* JSON trace logs
* Consistency & workflow metrics

---

## 🤖 Optional: Running with Real LLMs

### **Gemini**

```bash
set LLM_PROVIDER=gemini
set GOOGLE_API_KEY=your_key_here
```

### **OpenAI**

```bash
set LLM_PROVIDER=openai
set OPENAI_API_KEY=your_key_here
```

Run with:

```bash
python src/agent_orchestrator.py --demo
```

---

## 🚢 Deployment

### **Docker Build**

```bash
docker build -t smartsupport .
```

### **Docker Run**

```bash
docker run -p 8080:8080 smartsupport
```

### **Cloud Run Deployment**

Full deployment guide available inside the repo.

---

## 📅 Roadmap

* Vector database retrieval (FAISS / Pinecone / Weaviate)
* API server mode
* Real-time analytics dashboard
* Human feedback training loop
* SLA-aware prioritization
* Multi-turn conversation support

---

## 📝 License

Licensed under the **MIT License** — free to use, modify, and distribute.

---

## 👨‍💻 Author

**Akshit Kumar**

GitHub: [https://github.com/akshit40](https://github.com/akshit40)

Project: *SmartSupport PRO+* (Kaggle × Google Agents Capstone)

---

## ⭐ Support the Project

If you find this helpful, please **star the repo** — it encourages future improvements!

⭐ **Star →** [https://github.com/akshit40/smartsupport-pro-plus](https://github.com/akshit40/smartsupport-pro-plus)











