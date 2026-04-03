import re

def analyze_document_content(text):
    # 1. Simple Sentiment (Based on keyword density)
    positive_words = ['success', 'secure', 'improved', 'growth', 'positive', 'resolved']
    negative_words = ['breach', 'attack', 'fail', 'leak', 'incident', 'negative', 'error']
    
    pos_count = sum(1 for word in positive_words if word in text.lower())
    neg_count = sum(1 for word in negative_words if word in text.lower())

    sentiment = "Neutral"
    if pos_count > neg_count: sentiment = "Positive"
    elif neg_count > pos_count: sentiment = "Negative"

    # 2. Summary (First 2 sentences)
    # We clean the text of weird characters first
    clean_text = " ".join(text.split())
    sentences = clean_text.split('.')
    summary = ". ".join(sentences[:2]).strip() + "."

    # 3. Entities (Regex for capitalized names/orgs and years)
    # Finds words like "Microsoft", "March", "Cybersecurity Incident"
    found_entities = list(set(re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', text)))
    years = list(set(re.findall(r'\b(19|20)\d{2}\b', text)))
    
    return {
        "summary": summary,
        "entities": (found_entities[:8] + years[:3]),
        "sentiment": sentiment,
        "engine": "Static Analysis"
    }