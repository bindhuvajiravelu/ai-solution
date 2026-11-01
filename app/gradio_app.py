import gradio as gr
import joblib
import os

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(MODEL_PATH)

def classify_ticket(text):
    if not text.strip():
        return "Please enter a ticket"
    pred = model.predict([text])[0]
    return pred.upper()

demo = gr.Interface(
    fn=classify_ticket,
    inputs=gr.Textbox(lines=3, placeholder="My payment failed...", label="Support Ticket"),
    outputs=gr.Label(label="Predicted Category"),
    title="🤖 AI Support Ticket Classifier",
    examples=[["My payment failed"], ["I can't login"], ["App crashing"]]
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=10000)