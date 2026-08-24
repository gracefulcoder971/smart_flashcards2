import PyPDF2

def clean_file(filepath):
    text = ""
    if filepath.endswith(".pdf"):
        with open(filepath, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()
    text = text.replace("\n", " ").strip()
    return text
