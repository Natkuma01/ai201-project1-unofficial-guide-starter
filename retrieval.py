import os
import chromadb
from chromadb.utils import embedding_functions
# Import your previous code to get the chunks automatically
from ingest import load_and_clean_documents, chunk_text

def setup_vector_store(chunks):
    """Initializes ChromaDB locally, creates a collection, and stores embedded chunks."""
    # Create a local database folder in your project directory
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    
    # Setup the open-source embedding model function for ChromaDB
    # It automatically handles downloading and running all-MiniLM-L6-v2 locally
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Create or get the collection for our SNHU professor reviews
    collection = chroma_client.get_or_create_collection(
        name="snhu_cs_reviews",
        embedding_function=embedding_func
    )
    
    # Prepare data arrays for bulk loading into ChromaDB
    documents = []
    metadatas = []
    ids = []
    
    for idx, chunk in enumerate(chunks):
        documents.append(chunk["text"])
        metadatas.append(chunk["metadata"])
        ids.append(f"id_chunk_{idx}")
        
    # Load everything into the database
    print(f"Embedding and loading {len(documents)} chunks into local ChromaDB...")
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print("Database built successfully!")
    return collection

def query_vector_store(collection, query_text, top_k=4):
    """Searches the database for the most relevant text chunks."""
    results = collection.query(
        query_texts=[query_text],
        n_results=top_k
    )
    return results

if __name__ == "__main__":
    # 1. Gather chunks from Milestone 3
    raw_docs = load_and_clean_documents("data")
    chunks = chunk_text(raw_docs, chunk_size=500, overlap=100)
    
    # 2. Build the database
    collection = setup_vector_store(chunks)
    
    # 3. Test Retrieval with 3 of your Evaluation Plan queries
    test_queries = [
        "Which SNHU Computer Science professors are known for giving detailed, helpful feedback on coding projects?",
        "Is there a specific professor for CS-410 (Programming Languages) who is highly recommended?",
        "Which professors should I avoid generally?"
    ]
    
    print("\n==============================================")
    print("        RUNNING RETRIEVAL CHECKPOINT          ")
    print("==============================================\n")
    
    for q_idx, query in enumerate(test_queries, start=1):
        print(f"🔍 TEST QUERY #{q_idx}: '{query}'")
        print("-" * 50)
        
        # Search the database for top 4 matches
        search_results = query_vector_store(collection, query, top_k=4)
        
        # Extract returned matching data
        docs = search_results['documents'][0]
        metas = search_results['metadatas'][0]
        distances = search_results['distances'][0]
        
        for rank, (doc, meta, dist) in enumerate(zip(docs, metas, distances), start=1):
            print(f"  Match {rank} | Source: {meta['source']} | Distance Score: {dist:.4f}")
            print(f"  Content: {doc}")
            print("  .")
        print("=" * 60 + "\n")