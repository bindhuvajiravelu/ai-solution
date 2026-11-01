import os
import pickle
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

ENTITY_ALIASES = {
    "Mahatma Gandhi": ["india's father", "indias father", "father of india", "father of nation", "bapu", "m k gandhi", "m.k. gandhi", "mohandas karamchand", "mk gandhi"],
    "Indira Gandhi": ["indira", "mrs gandhi", "indira g"],
    "Jawaharlal Nehru": ["nehru", "chacha nehru", "pandit nehru", "jawaharlal"],
    "Sardar Patel": ["patel", "sardar", "vallabhbhai"],
}

def expand_query(question: str) -> str:
    low = question.lower()
    expanded = question
    for canonical, aliases in ENTITY_ALIASES.items():
        for alias in aliases:
            if alias in low:
                expanded += f" {canonical} {' '.join(aliases)}"
                print(f"Alias matched: '{alias}' -> {canonical}")
                break
    return expanded

class RAGChain:
    def __init__(self, vector_path="data/vectorstore.pkl"):
        print(f"Loading vectorstore from: {vector_path}")

        if not os.path.exists(vector_path):
            print(f"WARNING: {vector_path} not found. Running in empty mode.")
            self.chunks = []
            self.vectorizer = None
            self.vectors = None
            self.db = None
            self.vectorstore = None
            return

        with open(vector_path, "rb") as f:
            data = pickle.load(f)

            if isinstance(data, dict):
                self.chunks = data.get('chunks') or data.get('texts') or data.get('documents')
                self.vectorizer = data.get('vectorizer') or data.get('tfidf') or data.get('model')
                self.vectors = data.get('vectors') or data.get('embeddings')
                self.db = None
            elif isinstance(data, tuple):
                print(f"Tuple length: {len(data)}")
                if len(data) == 2:
                    self.chunks, self.vectorizer = data
                    self.vectors = None
                    self.db = None
                elif len(data) == 3:
                    self.chunks, self.vectors, self.vectorizer = data
                    self.db = None
                else:
                    self.chunks = data[0]
                    self.vectorizer = data[-1]
                    self.vectors = None
                    self.db = None
            else:
                self.db = data
                self.chunks = None
                self.vectorizer = None
                self.vectors = None
                print("Loaded as DB object")
                return

        print(f"Loaded {len(self.chunks)} chunks!")

    def answer(self, question):
        from sklearn.metrics.pairwise import cosine_similarity

        expanded_q = expand_query(question)

        if hasattr(self, 'db') and self.db is not None:
            docs = self.db.similarity_search(expanded_q, k=5)
            context = "\n\n".join([d.page_content for d in docs])
        else:
            if self.vectorizer is None or not self.chunks:
                return "Vectorstore not found on server. Please upload data/vectorstore.pkl to GitHub."
            q_vec = self.vectorizer.transform([expanded_q])
            chunk_texts = [c[0] if isinstance(c, tuple) else str(c) for c in self.chunks]
            
            if self.vectors is not None:
                scores = cosine_similarity(q_vec, self.vectors)[0]
            else:
                chunk_vectors = self.vectorizer.transform(chunk_texts)
                scores = cosine_similarity(q_vec, chunk_vectors)[0]
                
            top_idx = scores.argsort()[-5:][::-1]
            context = "\n\n".join([chunk_texts[i] for i in top_idx])

        context = context.replace("\u202f", " ").replace("\n", " ")
        context = re.sub(r"np\.float64\(.*?\)", "", context)
        context = re.sub(r"\s+", " ", context)

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
        prompt = f"""You are an expert on the book 'India Since Independence'.
RULES:
- "India's Father Gandhi" / "Father of Nation" / "Bapu" = Mahatma Gandhi (M.K. Gandhi). He was assassinated Jan 30, 1948.
- If asked about his politics AFTER independence, state he died 5 months after 1947 and Nehru took over.
- Answer ONLY from context, but clean up language.
- Give 3-4 sentence clear English summary.

Context:
{context[:4000]}

Question: {question}
Clean Answer:"""

        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=500
        )
        return completion.choices[0].message.content