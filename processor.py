import pytesseract
from PIL import Image
import docx2txt
import fitz  # PyMuPDF
import os

# Optional: Mac/Linux path
if os.name == "posix":
    pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"


def clean_text(text):
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

        elif extension in [".jpg", ".jpeg", ".png"]:
            image = Image.open(file_path).convert("L")
            text = pytesseract.image_to_string(image, config="--psm 6")

        else:
            return ""

        return clean_text(text)

    except Exception as e:
        print(f"Extraction error: {e}")
        return ""