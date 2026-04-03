import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from processor import extract_text
from analyzer import analyze_document_content

app = FastAPI(title="Local Document Analyser")

@app.get("/")
def read_root():
    return {"status": "Online", "mode": "Local NLP (No API Key)"}

@app.post("/process-document")
async def process_document(file: UploadFile = File(...)):
    # 1. Basic validation
    extension = os.path.splitext(file.filename)[1].lower()
    if extension not in [".pdf", ".docx"]:
        raise HTTPException(status_code=400, detail="Only .pdf and .docx supported")

    # 2. Save file temporarily
    temp_path = f"temp_{file.filename}"
    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 3. Extract Text
        raw_text = extract_text(temp_path, extension)
        
        if not raw_text or len(raw_text.strip()) < 5:
            return {"filename": file.filename, "error": "Document appears to be empty or unreadable."}

        # 4. Analyze Text (Local NLP)
        analysis = analyze_document_content(raw_text)

        return {
            "filename": file.filename,
            "analysis": analysis
        }

    except Exception as e:
        return {"error": str(e)}
    
    finally:
        # Cleanup
        if os.path.exists(temp_path):
            os.remove(temp_path)