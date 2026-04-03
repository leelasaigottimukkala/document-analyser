import os
import base64
import uuid
from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel
from processor import extract_text
from analyzer import analyze_document_content
from fastapi.responses import RedirectResponse

@app.api_route("/", methods=["GET", "POST", "PUT", "DELETE"])
async def root_redirect(request: Request):
    # This catches any request to the base URL and sends it to the correct path
    return RedirectResponse(url="/api/document-analyze", status_code=307)

app = FastAPI()

# 1. SECRET KEY - Change this or set in Render Environment
API_KEY = "sk_track2_987654321"

class DocumentRequest(BaseModel):
    fileName: str
    fileType: str
    fileBase64: str

@app.post("/api/document-analyze")
async def analyze_document(request: DocumentRequest, x_api_key: str = Header(None)):
    # 1. API Key Validation (Requirement 6)
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # 2. Decode Base64 (Requirement 5)
    try:
        file_content = base64.b64decode(request.fileBase64)
        temp_filename = f"{uuid.uuid4()}_{request.fileName}"
        
        with open(temp_filename, "wb") as f:
            f.write(file_content)

        # 3. Extract & Analyze
        extension = f".{request.fileType.lower()}"
        raw_text = extract_text(temp_filename, extension)
        analysis = analyze_document_content(raw_text)

        os.remove(temp_filename) # Cleanup

        # 4. Final Response Format (Requirement 9)
        return {
            "status": "success",
            "fileName": request.fileName,
            "summary": analysis["summary"],
            "entities": {
                "names": analysis["names"],
                "dates": analysis["dates"],
                "organizations": analysis["organizations"],
                "amounts": analysis["amounts"]
            },
            "sentiment": analysis["sentiment"]
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/")
def health():
    return {"status": "active", "endpoint": "/api/document-analyze"}
