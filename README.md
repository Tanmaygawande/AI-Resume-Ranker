# AI-Powered Resume Ranker

A lightweight NLP/ML web application that compares a PDF resume with a job description and produces a similarity score plus matched and missing keywords.

## Project objective
The internship brief asks for an AI-powered resume ranker using NLP, PDF text extraction, TF-IDF, a scoring algorithm, and a web UI. This implementation follows that structure while keeping the project simple enough to understand and explain in an interview.

## Features
- Upload a PDF resume
- Paste a job description
- Extract resume text using `pypdf`
- Clean and normalize text
- TF-IDF vectorization with unigram/bigram features
- Cosine-similarity based score
- Matched and missing keyword display
- Simple Flask web interface
- No external API key required

## Folder structure
```text
AI_Resume_Ranker/
├── app.py
├── utils.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── sample_data/
│   ├── job_description.txt
│   └── resumes/
├── templates/index.html
├── static/style.css
├── tests/test_utils.py
└── REPORT.pdf
```

## Run locally
1. Install Python 3.10+.
2. Create an environment:
   `python -m venv .venv`
3. Activate it.
4. Install:
   `pip install -r requirements.txt`
5. Start:
   `python app.py`
6. Open `http://127.0.0.1:5000/`.
7. Paste the sample job description and upload any readable PDF resume.

## How the score works
The resume and job description are converted into TF-IDF vectors. Cosine similarity measures how close those vectors are. The displayed percentage is `cosine_similarity × 100`.

This is a screening-support prototype, not a replacement for human recruitment. A high score does not prove candidate quality.

## Testing
Run:
`python -m unittest discover tests`

## Dataset
No large dataset is bundled because the project operates on user-supplied resumes and job descriptions. A sample job description is included for demonstration.

## GitHub
Create a repository named `AI-Resume-Ranker`, then upload all files from this folder. Suggested description:
"Flask + NLP resume ranking system using TF-IDF and cosine similarity."

## Interview talking points
- Why TF-IDF instead of raw keyword counting?
- What does cosine similarity measure?
- How does preprocessing affect similarity?
- What are false positives/false negatives in resume screening?
- How could embeddings/BERT improve semantic matching?
- How would you deploy and monitor the application?
