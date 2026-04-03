# 📄 Document Structure & Sentiment Analyser

A lightweight, high-performance web API built with **FastAPI** that extracts text from documents (PDF & DOCX) and performs automated structural analysis, entity recognition, and sentiment detection using a custom **Local NLP Engine**.

---

## 🚀 Live Demo
**API Documentation (Swagger UI):** [https://document-analyser-d5e8.onrender.com/docs](https://document-analyser-d5e8.onrender.com/docs)

---

## ✨ Features
- **Multi-Format Support:** Seamlessly process `.pdf` and `.docx` files.
- **Privacy-First NLP:** Performs analysis locally on the server without sending data to third-party AI APIs (No API keys required).
- **Automated Summary:** Extracts key introductory context from uploaded documents.
- **Entity Recognition:** Identifies organizations, years, and key stakeholders using pattern-based extraction.
- **Sentiment Analysis:** Categorizes document tone as **Positive**, **Negative**, or **Neutral**.
- **Blazing Fast:** Optimized for low-latency processing on cloud environments like Render.

---

## 🛠️ Tech Stack
- **Framework:** FastAPI (Python)
- **Deployment:** Render (Cloud PaaS)
- **Libraries:** - `PyMuPDF` (High-speed PDF parsing)
  - `docx2txt` (Word document extraction)
  - `Uvicorn` (ASGI Server)
  - `python-multipart` (File upload handling)

---

## ⚙️ Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/leelasaigottimukkala/document-analyser.git](https://github.com/leelasaigottimukkala/document-analyser.git)
   cd document-analyser