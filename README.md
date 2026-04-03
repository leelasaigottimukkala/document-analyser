# Data Extraction API (Track 2)

## 📝 Description
This is an intelligent document processing system designed to extract, analyze, and summarize content from various document formats (PDF and DOCX). The system leverages a custom Natural Language Processing (NLP) strategy to understand document structure, extract key entities, and perform sentiment analysis without external API dependencies, ensuring data privacy and high-speed processing.

## 🚀 Live Deployed URL
**Base URL:** [https://document-analyser-d5e8.onrender.com](https://document-analyser-d5e8.onrender.com)  
**API Endpoint:** `POST /api/document-analyze`  
**Interactive Docs:** [https://document-analyser-d5e8.onrender.com/docs](https://document-analyser-d5e8.onrender.com/docs)

---

## 🛠️ Tech Stack
- **Framework:** FastAPI (Python 3.14)
- **Deployment:** Render (Cloud PaaS)
- **Key Libraries:** - `PyMuPDF (fitz)`: High-performance PDF text and layout extraction.
  - `docx2txt`: Structured extraction for Word documents.
  - `Pydantic`: Data validation and Base64 schema handling.
- **AI/ML Strategy:** Regex-based Named Entity Recognition (NER) and Lexicon-based Sentiment Analysis.

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

   git clone [https://github.com/leelasaigottimukkala/document-analyser.git](https://github.com/leelasaigottimukkala/document-analyser.git)
   cd document-analyser
   
2. Install dependencies:

pip install -r requirements.txt

3.Set Environment Variables:
Create a .env file or set the following in your environment:
API_KEY=sk_track2_987654321

4.Run the Application:
  uvicorn main:app --host 0.0.0.0 --port 10000

🧠 Approach & Strategy
1. Data Extraction
PDF: Uses fitz (PyMuPDF) to stream document bytes directly from memory, preserving text order.

DOCX: Processes XML-based document structures to extract clean text.

Base64 Handling: Decodes incoming strings into temporary binary streams for secure processing.

2. Summary Generation
Implements a Lead-Sentence Extraction algorithm. It identifies the most contextually relevant sentences at the start of the document to provide a concise summary.

3. Entity & Sentiment Analysis
Entities: Uses optimized Regular Expressions (Regex) to categorize:

Names: Title-case pattern matching.

Organizations: Identification of suffixes like "Pvt Ltd", "Corp", and "Inc".

Dates: Multi-format date recognition (DD Month YYYY, YYYY, etc.).

Amounts: Currency symbol detection (₹, $, USD, INR).

Sentiment: A statistical scoring engine that weights positive vs. negative tokens to classify the document tone.

📂 API Usage (Requirement 7)
Authentication
Requests must include the following header:
x-api-key: sk_track2_987654321

Request Example (cURL)
Bash
curl -X POST [https://document-analyser-d5e8.onrender.com/api/document-analyze](https://document-analyser-d5e8.onrender.com/api/document-analyze) \
  -H "Content-Type: application/json" \
  -H "x-api-key: sk_track2_987654321" \
  -d '{
    "fileName": "sample1.pdf",
    "fileType": "pdf",
    "fileBase64": "JVBERi0xLjQKJcfsj6IKNSAwIG9iago..."
  }'
Success Response (200 OK)
JSON
{
  "status": "success",
  "fileName": "sample1.pdf",
  "summary": "AI-generated summary text...",
  "entities": {
    "names": ["Ravi Kumar"],
    "dates": ["10 March 2026"],
    "organizations": ["ABC Pvt Ltd"],
    "amounts": ["₹10,000"]
  },
  "sentiment": "Positive"
}
