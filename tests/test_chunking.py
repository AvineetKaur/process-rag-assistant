from process_rag_assistant.ingestion.pdf_loader import load_pdf_pages
from process_rag_assistant.ingestion.chunker import chunk_pages


def test_chunking():
    pages = load_pdf_pages("data/raw", "test_process")
    chunks = chunk_pages(pages)

    assert len(pages) == 6
    assert len(chunks) == 12