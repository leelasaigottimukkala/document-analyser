# Data Extraction API - Track 2

## Description
This system is an intelligent document processor designed to extract text from PDF and DOCX formats. It uses a structured regex-based extraction strategy and Natural Language Processing (NLP) to identify entities, generate summaries, and classify sentiment without external API dependencies.

## Tech Stack
- **Language:** Python 3.14 (FastAPI)
- **Deployment:** Render (Publicly Accessible)
- **Libraries:** PyMuPDF (fitz), docx2txt, Pydantic
- **AI Strategy:** Pattern-based Entity Recognition and Statistical Sentiment Analysis.

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Run Application:** `uvicorn main:app --host 0.0.0.0 --port 10000`

## Approach
- **Extraction:** Uses PyMuPDF for layout-aware PDF text extraction and docx2txt for XML-based DOCX parsing.
- **Summary:** Implements a lead-sentence extraction algorithm to identify the primary context.
- **Entities:** Utilizes Regular Expressions (Regex) to categorize Names, Dates, Organizations, and Monetary amounts (₹/$).
- **Sentiment:** A lexicon-based scoring system analyzes the emotional tone of the content.

## API Endpoint
**POST** `https://document-analyser-d5e8.onrender.com/api/document-analyze`
**Header:** `x-api-key: sk_track2_987654321`
