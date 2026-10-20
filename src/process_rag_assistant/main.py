from process_rag_assistant.ingestion.pdf_loader import load_pdf_pages
from process_rag_assistant.ingestion.chunker import chunk_pages
from process_rag_assistant.embeddings.embedder import generate_embeddings,  generate_query_embedding
from process_rag_assistant.vector_store.chroma_store import create_collection,store_embeddings
from process_rag_assistant.retrieval.retriever import retrieve_chunks,display_retrieval_results
from process_rag_assistant.retrieval.retriever import retrieve_chunks
from process_rag_assistant.generation.context_builder import build_context

from pathlib import Path

def main():
    print("Starting RAG pipeline...")
    #Load pdf
    documents_directory = Path("data/raw")

    #extract text
    pages = load_pdf_pages(
        pdf_directory=documents_directory,
        process_id="ORION-ONB-01",
    )

    #chunk text
    chunks=chunk_pages(pages)
    for chunk in chunks[:5]:
        print(chunk["chunk_id"])

    #generate embeddings
    embeddings =generate_embeddings(chunks)

    # Validate results
    chunk_ids = [chunk["chunk_id"] for chunk in chunks]
    print("Total pages:", len(pages))
    print("Total chunks:", len(chunk_ids))
    print("Embeddings shape:", embeddings.shape)

    #store embeddings in chromaDB
    collection=create_collection()
    store_embeddings(collection,chunks, embeddings)

    print("Stored chunks:", collection.count())

    questions="What happens when customer verification fails?"
    embedded_query= generate_query_embedding(questions)
    results=retrieve_chunks(collection,embedded_query)
    # display_retrieval_results(results)
    chunks=build_context(results)
    print(chunks)
 


if __name__ == "__main__":
    main()