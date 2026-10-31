import joblib
import os

class Classifier:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            self.model = None # fallback if model not trained yet

    def clean_text(self, text):
        return text.lower().strip() if text else ""

    def predict(self, text):
        cleaned = self.clean_text(text)
        if not cleaned:
            return "unknown"
        
        if self.model:
            return self.model.predict([cleaned])[0]
        
        # fallback to your old rules if model missing
        if "urgent" in cleaned:
            return "urgent"
        if "bug" in cleaned or "error" in cleaned:
            return "bug"
        return "unknown"