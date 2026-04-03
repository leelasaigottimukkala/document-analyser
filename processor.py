import fitz  # PyMuPDF
import docx2txt

def clean_text(text):
    if not text:
        return ""
    return " ".join(text.split())

def extract_text(file_path, extension):
    try:
        text = ""
        if extension == ".pdf":
            doc = fitz.open(file_path)
            for page in doc:
                text += page.get_text("text") + "\n"
            doc.close()

        elif extension == ".docx":
            text = docx2txt.process(file_path)

        else:
            return "Unsupported file format for this engine."

        return clean_text(text)

    except Exception as e:
        print(f"Extraction error: {e}")
        return ""
