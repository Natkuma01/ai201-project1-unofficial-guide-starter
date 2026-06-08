import os
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
import gradio as gr
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# 1. Initialize Local Database connection
chroma_client = chromadb.PersistentClient(path="./chroma_db")
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
collection = chroma_client.get_or_create_collection(
    name="snhu_cs_reviews", 
    embedding_function=embedding_func
)

# 2. Initialize the Groq LLM Client
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ask_unofficial_guide(question):
    """
    Retrieves relevant blocks from ChromaDB, feeds them to Llama 3.3 via Groq,
    and returns a strictly grounded answer with programmatically verified sources.
    """
    # Search ChromaDB for the top 4 matching chunks
    search_results = collection.query(
        query_texts=[question],
        n_results=4
    )
    
    # Extract documents and metadata
    retrieved_chunks = search_results['documents'][0]
    retrieved_metas = search_results['metadatas'][0]
    
    # Format the retrieved text into a single clean block of context
    context_text = ""
    unique_sources = set()
    
    for idx, (chunk_text, meta) in enumerate(zip(retrieved_chunks, retrieved_metas), start=1):
        context_text += f"[Document fragment #{idx} from source: {meta['source']}]\n{chunk_text}\n\n"
        unique_sources.add(meta['source'])
        
    # Create a strict system prompt to completely block hallucinations
    system_prompt = (
        "You are an assistant for the Unofficial Guide to SNHU Computer Science professors.\n"
        "Your absolute core directive is to answer the user's question using ONLY the provided text fragments.\n"
        "Strict Guidelines:\n"
        "1. Rely exclusively on the clear facts mentioned directly in the fragments.\n"
        "2. Do NOT use outside general knowledge or assumptions about professors.\n"
        "3. If the provided text fragments do not contain enough specific facts to answer the question, "
        "you must respond word-for-word with: 'I do not have enough information on that based on student reviews.'\n"
        "4. Keep your response factual, concise, and professional."
    )
    
    user_prompt = f"Context text fragments:\n{context_text}\nUser Question: {question}"
    
    # Send the payload to Groq using the fast llama-3.3-70b-versatile model
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.0 # Force zero randomness for maximum accuracy
    )
    
    llm_answer = chat_completion.choices[0].message.content
    
    # Return both the text answer and the structured source list
    return {
        "answer": llm_answer,
        "sources": sorted(list(unique_sources))
    }

def handle_query(question):
    """Bridge function connecting the Gradio UI text boxes to our backend code."""
    if not question.strip():
        return "Please type a question.", ""
        
    result = ask_unofficial_guide(question)
    
    # Format list of sources into bullet points
    sources_bullet_list = "\n".join(f"• {source_file}" for source_file in result["sources"])
    
    return result["answer"], sources_bullet_list

# 4. Build the Gradio UI web interface layout
with gr.Blocks(title="SNHU CS Unofficial Guide") as demo:
    gr.Markdown("# 🎓 SNHU Computer Science Professor Guide")
    gr.Markdown("Search local student reviews from Reddit and RateMyProfessors instantly.")
    
    with gr.Row():
        with gr.Column():
            inp = gr.Textbox(
                label="Ask a question about a professor or course workload:", 
                placeholder="e.g., How accessible is Professor Proske or what do students say about assignments?",
                lines=2
            )
            btn = gr.Button("Search & Generate Answer", variant="primary")
            
    with gr.Row():
        with gr.Column():
            answer_box = gr.Textbox(label="Grounded AI Answer", lines=8, interactive=False)
            sources_box = gr.Textbox(label="Verified Source Files Consulted", lines=4, interactive=False)
            
    # Set up triggers for clicking the button or pressing enter inside the text field
    btn.click(handle_query, inputs=inp, outputs=[answer_box, sources_box])
    inp.submit(handle_query, inputs=inp, outputs=[answer_box, sources_box])

if __name__ == "__main__":
    # Launch the local web server
    demo.launch()