from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

class SimpleVectorStore:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
        self.chunks = []
        self.vectors = None

    def build(self, chunks):
        print(f"Building TF-IDF for {len(chunks)} chunks... RAM usage will be low")
        self.chunks = chunks
        self.vectors = self.vectorizer.fit_transform(chunks)
        print("Done!")
        # Save to avoid rebuilding
        with open("data/vectorstore.pkl", "wb") as f:
            pickle.dump((self.chunks, self.vectors, self.vectorizer), f)

    def search(self, query, top_k=3):
        from sklearn.metrics.pairwise import cosine_similarity
        q_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(q_vec, self.vectors).flatten()
        top_indices = scores.argsort()[-top_k:][::-1]
        return [(self.chunks[i], scores[i]) for i in top_indices]

# Test
if __name__ == "__main__":
    from loader import load_and_chunk_pdf
    chunks = load_and_chunk_pdf("data/India_Independence.pdf")
    # Use only first 500 chunks for testing to keep RAM low
    store = SimpleVectorStore()
    store.build(chunks[:500]) 
    results = store.search("What was Nehruvian agenda?")
    for chunk, score in results:
        print(f"\nScore {score:.2f}: {chunk[:300]}...")