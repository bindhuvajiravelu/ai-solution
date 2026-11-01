import os
import sys
import gradio as gr

# Fix import path for both local and Render
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "app"))

from rag_chain import RAGChain

rag = RAGChain()

def chat_fn(question):
    if not question.strip():
        return "Please ask a question!"
    return rag.answer(question)

with gr.Blocks(title="RAG Bot - India Since Independence") as demo:
    gr.Markdown("## 📚 RAG Bot - Ask from 'India Since Independence' book")
    inp = gr.Textbox(label="Your Question", placeholder="What was Nehruvian agenda?")
    out = gr.Textbox(label="Answer", lines=10)
    btn = gr.Button("Ask")
    btn.click(chat_fn, inputs=inp, outputs=out)
    inp.submit(chat_fn, inputs=inp, outputs=out)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))