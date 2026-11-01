RAG BOT - Ask from 'India Since Independence' Book

Live URL: https://ai-solution-1-qlhx.onrender.com

PROJECT OVERVIEW

This is a Retrieval-Augmented Generation (RAG) chatbot that answers questions ONLY from the book 'India Since Independence'. It searches the book's vector database and answers from context.

TECH STACK

- Python
- TF-IDF Vector Store (sklearn) - data/vectorstore.pkl
- Gradio for Web UI - app/ui.py
- LLM for answer generation
- Deployed on Render.com

PROJECT STRUCTURE

app/
├── rag_chain.py      # Brain - Retrieval + LLM + Alias Logic
└── ui.py             # Face - Gradio Web Server
data/
├── book.pdf
└── vectorstore.pkl   # Must be pushed with git add -f
requirements.txt
README.txt

KEY FEATURES

1. Alias Expansion: bapu, father's nation, india's father -> mahatma gandhi
2. Cloud-Ready: os.path.exists() check for vectorstore.pkl
3. Gradio production: Start Command = python app/ui.py

HOW TO RUN LOCALLY

pip install -r requirements.txt
python app/ui.py

HOW TO DEPLOY

git add -f data/vectorstore.pkl
git commit -m "add vectorstore"
git push
Render -> Build: pip install -r requirements.txt
Render -> Start: python app/ui.py

SAMPLE QUESTIONS

- when gandhi died
- when india's father died
- what is nehru's role in early years
