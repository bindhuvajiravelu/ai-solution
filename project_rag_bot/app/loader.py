import os
from pypdf import PdfReader

def load_and_chunk_pdf(pdf_path, chunk_size=500, chunk_overlap=200):
    """Loads your Bipan Chandra PDF and chunks it"""
    print(f"Loading PDF: {pdf_path}")
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    
    print(f"Total characters: {len(full_text)}")
    
    # Simple chunking
    chunks = []
    start = 0
    while start < len(full_text):
        end = start + chunk_size
        chunks.append(full_text[start:end])
        start += chunk_size - chunk_overlap
    
    print(f"Created {len(chunks)} chunks")
    return chunks

if __name__ == "__main__":
    # Test it
    pdf_path = "../data/GS1_PI_India_Since_Independence_Bipan_Chandra.pdf"
    # or if you put PDF in root data folder:
    # pdf_path = "../../data/GS1_PI_India_Since_Independence_Bipan_Chandra.pdf"
    if os.path.exists(pdf_path):
        chunks = load_and_chunk_pdf(pdf_path)
        print(f"\nFirst chunk preview:\n{chunks[0][:500]}")
    else:
        print(f"Please copy your PDF to: {pdf_path}")