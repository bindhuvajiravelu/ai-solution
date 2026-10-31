class Classifier:
    def predict(self, text:str) -> str:
        text = text.lower().strip()

        if not text:
            return "unknown"
        if "urgent" in text or "asap" in text:
            return "urgent"
        elif "bug" in text or "error" in text or "fix" in text:
            return "bug"
        elif "feature" in text or "request" in text:
            return "feature"
        else:
            return "general"
        