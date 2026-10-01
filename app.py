from flask import Flask, render_template, request
from pathlib import Path
from werkzeug.utils import secure_filename
from utils import extract_text_from_pdf, rank_resume

app = Flask(__name__)
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
ALLOWED = {".pdf"}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        job_description = request.form.get("job_description", "").strip()
        resume = request.files.get("resume")
        if not job_description:
            error = "Please enter a job description."
        elif not resume or not resume.filename:
            error = "Please upload a PDF resume."
        elif Path(resume.filename).suffix.lower() not in ALLOWED:
            error = "Only PDF resumes are supported."
        else:
            filename = secure_filename(resume.filename)
            path = UPLOAD_DIR / filename
            resume.save(path)
            try:
                resume_text = extract_text_from_pdf(path)
                if not resume_text.strip():
                    raise ValueError("No readable text was found in the PDF.")
                result = rank_resume(resume_text, job_description)
            except Exception as exc:
                error = f"Could not process the resume: {exc}"
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
