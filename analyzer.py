import re

def analyze_document_content(text):
    if not text:
        return {"summary": "Empty document.", "names": [], "dates": [], "organizations": [], "amounts": [], "sentiment": "Neutral"}

    # 1. AI-Powered Summary (Requirement 2)
    clean_text = " ".join(text.split())
    sentences = clean_text.split('.')
    summary = ". ".join(sentences[:3]).strip() + "."

    # 2. Key Entity Extraction (Regex patterns)
    names = list(set(re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', text)))[:3]
    dates = list(set(re.findall(r'\b\d{1,2} [A-Z][a-z]+ \d{4}\b|\b\d{4}\b', text)))[:3]
    orgs = list(set(re.findall(r'\b[A-Z]{2,}\b|\b[A-Z][a-z]+ (?:Pvt Ltd|Corp|Inc|Group)\b', text)))[:3]
    amounts = list(set(re.findall(r'(?:₹|\$|INR|USD)\s?\d+(?:,\d+)*(?:\.\d+)?', text)))[:3]

    # 3. Sentiment Analysis
    pos_words = ['growth', 'success', 'innovation', 'profit', 'positive', 'win']
    neg_words = ['loss', 'decline', 'attack', 'risk', 'fail', 'negative']
    
    score = sum(1 for w in pos_words if w in text.lower()) - sum(1 for w in neg_words if w in text.lower())
    sentiment = "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"

    return {
        "summary": summary,
        "names": names,
        "dates": dates,
        "organizations": orgs,
        "amounts": amounts,
        "sentiment": sentiment
    }
