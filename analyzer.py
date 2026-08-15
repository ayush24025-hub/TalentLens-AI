import io
import re
from pathlib import Path
import docx2txt
import pdfplumber

SKILLS = [
    "python","java","c++","c","sql","mysql","postgresql","mongodb","flask","django",
    "fastapi","rest api","api","git","github","docker","aws","azure","gcp",
    "machine learning","deep learning","nlp","natural language processing",
    "data analysis","pandas","numpy","scikit-learn","tensorflow","pytorch",
    "html","css","javascript","react","node.js","express","power bi","tableau",
    "excel","communication","problem solving","leadership"
]

def extract_text(uploaded_file):
    data = uploaded_file.getvalue()
    name = uploaded_file.name.lower()
    if name.endswith(".pdf"):
        with pdfplumber.open(io.BytesIO(data)) as pdf:
            return "\n".join((p.extract_text() or "") for p in pdf.pages)
    if name.endswith(".docx"):
        return docx2txt.process(io.BytesIO(data))
    raise ValueError("Only PDF and DOCX files are supported.")

def normalize(text):
    return re.sub(r"\s+", " ", text.lower()).strip()

def find_skills(text):
    t = normalize(text)
    found = []
    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"
        if re.search(pattern, t):
            found.append(skill)
    return sorted(set(found))

def extract_keywords(jd):
    t = normalize(jd)
    return find_skills(t)

def analyze_resume(filename, text, jd):
    resume_skills = find_skills(text)
    required = extract_keywords(jd)
    matched = sorted(set(resume_skills) & set(required))
    missing = sorted(set(required) - set(resume_skills))

    skill_score = round((len(matched) / len(required) * 100) if required else 0)
    keyword_score = skill_score

    jd_terms = set(re.findall(r"[a-zA-Z]{3,}", normalize(jd)))
    resume_terms = set(re.findall(r"[a-zA-Z]{3,}", normalize(text)))
    overlap = len(jd_terms & resume_terms) / max(1, len(jd_terms))
    relevance_score = round(min(100, overlap * 100))

    return {
        "candidate": Path(filename).stem.replace("_", " ").replace("-", " ").title(),
        "text": text,
        "resume_skills": resume_skills,
        "required_skills": required,
        "matched_skills": matched,
        "missing_skills": missing,
        "skill_score": skill_score,
        "keyword_score": keyword_score,
        "relevance_score": relevance_score,
    }
