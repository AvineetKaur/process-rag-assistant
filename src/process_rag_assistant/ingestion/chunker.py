

def chunk_pages(pages, chunk_size=200, overlap=20):
    chunks=[]
    for page in pages:
        text=page["text"]
        words=text.split()
        start=0
        chunk_id=0
        while start<len(words):
            chunk_id+=1
            end=start+chunk_size
            chunk_words=words[start:end]
            chunk_words=" ".join(chunk_words)
            chunks.append({
                "text":chunk_words,
                "process_id": page["process_id"],
                "document_name":page["document_name"],
                "page_number":page["page_number"],
                "chunk_id":chunk_id
            })
            start=end-overlap
    return chunks

