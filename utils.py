import re
from pathlib import Path
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

STOP_WORDS = {
    "the","and","for","with","that","this","from","are","you","your","our",
    "have","has","will","into","using","use","job","role","work","years",
    "about","their","they","them","also","who","what","where","when"
}

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(str(pdf_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def clean_text(text):
    text = re.sub(r"[^a-zA-Z0-9+#.\- ]+", " ", text.lower())
    tokens = [t for t in text.split() if t not in STOP_WORDS]
    return " ".join(tokens)

def keywords(text, top_n=20):
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9+#.\-]{2,}", text.lower())
    common = [w for w in words if w not in STOP_WORDS]
    seen = []
    for word in common:
        if word not in seen:
            seen.append(word)
    return seen[:top_n]

def rank_resume(resume_text, job_description):
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_description)
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
    matrix = vectorizer.fit_transform([resume_clean, job_clean])
    similarity = float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0])
    score = round(similarity * 100, 2)

    resume_tokens = set(resume_clean.split())
    job_tokens = set(job_clean.split())
    matched = sorted(resume_tokens & job_tokens)
    missing = sorted(job_tokens - resume_tokens)

    return {
        "score": score,
        "matched_keywords": matched[:25],
        "missing_keywords": missing[:25],
        "recommendation": (
            "Strong keyword/content match" if score >= 70 else
            "Moderate match - review missing skills" if score >= 45 else
            "Low match - resume needs stronger alignment"
        )
    }
