def build_context(text_results):
    documents=text_results["documents"][0]
    metadatas=text_results["metadatas"][0]
    context_parts=[]
    for start,(doc,met) in enumerate(
        zip(documents,metadatas),start=1):

        formatted_chunk=f"[Source {start}]\nDocument:{met['document_name']}\nPage:{met['page_number']}\nContent:{doc}"
        context_parts.append(formatted_chunk)

    result="\n\n".join(context_parts)
    return result

