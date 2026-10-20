
def retrieve_chunks(collection, query_embedding, top_k=3):
    result=collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"])
    return result

def display_retrieval_results(results):
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for index, (document, metadata, distance) in enumerate(
        zip(documents, metadatas, distances), start=1
    ):
        print(f"\n{'=' * 50}")
        print(f"Result {index}")
        print(f"{'=' * 50}")

        print(f"Document: {metadata['document_name']}")
        print(f"Page: {metadata['page_number']}")
        print(f"Process ID: {metadata['process_id']}")
        print(f"Distance: {distance:.4f}")

        print("\nRetrieved Text:")
        print(document)