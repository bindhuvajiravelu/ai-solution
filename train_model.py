from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# 1. Your training data - start small, you can expand later
X_train = [
    "This is urgent need help",
    "urgent server down",
    "There is a bug error",
    "bug in login page",
    "feature request new button",
    "hello how are you",
    ""
]
y_train = ["urgent", "urgent", "bug", "bug", "feature", "unknown", "unknown"]

# 2. Pipeline: TF-IDF + Logistic Regression
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

model.fit(X_train, y_train)

# 3. Save
joblib.dump(model, "app/model.pkl")
print("Model saved to app/model.pkl, accuracy on train:", model.score(X_train, y_train))

