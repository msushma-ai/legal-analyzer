import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    """
    Extracts text from a PDF file or uploaded file object.
    """
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") if hasattr(file, "read") else fitz.open(file) as pdf:
        for page in pdf:
            text += page.get_text("text")
    return text.strip()
