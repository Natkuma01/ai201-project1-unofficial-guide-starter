import os
import glob

def load_and_clean_documents(data_path="data"):
    """Loads all text files from the data folder and applies basic cleanup."""
    documents = {}
    # Find all .txt files in the specified folder
    file_pattern = os.path.join(data_path, "*.txt")
    file_paths = glob.glob(file_pattern)
    
    if not file_paths:
        print(f"Warning: No .txt files found in '{data_path}' folder!")
        print("Please make sure you created the folder and added files like doc1.txt, doc2.txt, etc.")
        return documents

    for path in file_paths:
        filename = os.path.basename(path)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
            
            # Basic Ingestion Cleaning: Remove massive chunks of blank lines/spaces
            cleaned_text = " ".join(text.split())
            
            documents[filename] = cleaned_text
            
    print(f"Successfully loaded and cleaned {len(documents)} documents.")
    return documents

def chunk_text(documents, chunk_size=500, overlap=100):
    """Splits document text into chunks based on character count and overlap."""
    all_chunks = []
    
    for filename, text in documents.items():
        start = 0
        text_length = len(text)
        doc_chunks_count = 0
        
        # Slide a window across the text string
        while start < text_length:
            end = start + chunk_size
            chunk_content = text[start:end].strip()
            
            # Guardrail: Avoid saving empty strings as chunks
            if len(chunk_content) > 0:
                all_chunks.append({
                    "text": chunk_content,
                    "metadata": {"source": filename}
                })
                doc_chunks_count += 1
                
            # Move the window forward by chunk_size minus the overlap
            start += (chunk_size - overlap)
            
    return all_chunks

if __name__ == "__main__":
    # 1. Run the loading and cleaning pipeline
    raw_docs = load_and_clean_documents("data")
    
    if raw_docs:
        # 2. Run the chunking strategy
        chunks = chunk_text(raw_docs, chunk_size=500, overlap=100)
        
        print(f"Total chunks generated across all documents: {len(chunks)}\n")
        print("--- INSPECTING 5 REPRESENTATIVE CHUNKS ---")
        
        # 3. Print 5 representative chunks for inspection checkpoint
        sample_chunks = chunks[:5] if len(chunks) >= 5 else chunks
        for idx, chunk in enumerate(sample_chunks, start=1):
            print(f"\n[Chunk #{idx}] | Source: {chunk['metadata']['source']} | Length: {len(chunk['text'])} chars")
            print(f"Content: {chunk['text']}")
            print("-" * 40)