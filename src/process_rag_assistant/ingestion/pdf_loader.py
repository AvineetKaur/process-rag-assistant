from pathlib import Path
from pypdf import PdfReader


def load_pdf_pages(pdf_directory,process_id,) -> list[dict]:
    """Extract page-level records from PDFs in a directory."""

    page_records =[]

    # Find every PDF in pdf_directory.
    pdf_files = Path(pdf_directory).glob("*.pdf")

    # Loop through the PDF paths.
    for pdf_path in pdf_files:
        reader = PdfReader(pdf_path)
        #Iterate through its pages.
        for page_number, page in enumerate(reader.pages, start=1):
            #  Extract the text.
            text = page.extract_text() or ""

            # Add a dictionary to page_records.
            page_records.append(
                {
                    "process_id": process_id,
                    "document_name": pdf_path.name,
                    "page_number": page_number,
                    "text": text,
                }
            )

    return page_records


if __name__ == "__main__":
    documents_directory = Path("data/raw")

    pages = load_pdf_pages(
        pdf_directory=documents_directory,
        process_id="ORION-ONB-01",
    )

    print(f"Extracted {len(pages)} pages")
    print("Python started from:", Path.cwd())
    print("PDF directory:", documents_directory.resolve())

    for page in pages:
        print(
            page["document_name"],
            page["page_number"],
            repr(page["text"][:100]),
        )