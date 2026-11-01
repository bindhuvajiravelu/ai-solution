# ai-solution

# 🤖 AI Support Ticket Classifier

> Production-grade NLP system that auto-classifies customer support tickets into Billing, Technical, Account & General categories.

**Live Demo:**
- 🚀 **API (Swagger UI):** https://ai-support-classifier.onrender.com/docs
- 🎨 **Gradio UI:** 🚀 Live Demo: https://ai-solution-kve5.onrender.com/
- 💻 **GitHub:** https://github.com/bindhuvajiravelu/ai-solution
---

### 📌 Problem Statement
Customer support teams receive thousands of unstructured tickets daily. Manual routing is slow and error-prone. This system automates ticket categorization using NLP to reduce response time and improve routing accuracy.

### 🏗️ Architecture
User Ticket (Text)
      |
      v
[Gradio UI]  ---->  [FastAPI /predict]  ---->  [TF-IDF + scikit-learn Model]
      |                     |                              |
      v                     v                              v
Label Display         JSON Response               model.pkl (Trained)
      |
[Render + HuggingFace Deployment]


### ✨ Features
- **NLP Model:** TF-IDF Vectorizer + MultinomialNB / LogisticRegression classifier
- **REST API:** FastAPI with Pydantic validation, auto OpenAPI docs at `/docs`
- **Interactive UI:** Gradio interface with example prompts for non-technical users
- **Testing:** Pytest suite with 100% endpoint coverage
- **Deployment Ready:** Deployed on Render (API) & Hugging Face Spaces (UI)
- **Latency:** <200ms inference time

### 🛠️ Tech Stack
- **Language:** Python 3.11
- **ML:** scikit-learn, NumPy, joblib
- **API:** FastAPI, Uvicorn
- **UI:** Gradio
- **Testing:** pytest, httpx
- **Deployment:** Render, Hugging Face Spaces, Git

### 📁 Project Structure
ai-solution/
├── app/
│   ├── main.py          # FastAPI app - /predict & /docs
│   ├── classifier.py    # predict() logic & model loading
│   ├── model.pkl        # Trained model artifact
│   ├── vectorizer.pkl   # TF-IDF vectorizer
│   └── app_ui.py        # Gradio UI for end users
├── tests/
│   └── test_main.py     # API & model tests
├── requirements.txt
├── .gitignore
└── README.md


### 🚀 Quick Start (Local)

1. Clone & setup venv:
```bash
git clone https://github.com/bindhuvajiravelu/ai-solution.git
cd ai-support-classifier
python -m venv venv
venv\Scripts\activate  # Windows

2. Install dependencies:
pip install -r requirements.txt

3. Run API:
uvicorn app.main:app --reload
# Open http://127.0.0.1:8000/docs

4. Run Gradio UI:
python app/app_ui.py
# Open http://127.0.0.1:7860

5. Test:
pytest -v

🔌 API Usage
Endpoint: POST /predictRequest:
Request:
{
  "text": "My payment failed twice"
}

Response:
{
  "label": "billing",
  "confidence": 0.94
}
cURL:
curl -X POST https://ai-support-classifier.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I cannot login"}'

📊 Model Details
Dataset: Custom support tickets (billing, technical, account, general)
Preprocessing: Lowercasing, TF-IDF Vectorization (max_features=5000)
Model: Scikit-learn classifier with probability scores
Artifacts: model.pkl & vectorizer.pkl loaded at runtime

🌐 DeploymentAPI:
Auto-deployed from GitHub main branch to Render
UI: Deploy app_ui.py to Hugging Face Spaces (Gradio SDK)
Environment variables managed via Render Dashboard

👨‍💻 AuthorYour Name — Aspiring AI Engineer | Python | ML | FastAPI
LinkedIn: https://www.linkedin.com/in/bindhukvajiravelu

📝 Future Improvements
Add BERT-based classifier for higher accuracy
Add confidence threshold & fallback to human
Dockerize for Kubernetes deployment
Add LangChain for auto-reply generation
