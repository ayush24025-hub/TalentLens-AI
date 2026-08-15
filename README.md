# 🎯 TalentLens AI

### Explainable AI-Based Resume Screening, Skill Gap Analysis & Candidate Ranking System

TalentLens AI is a practical NLP-based recruitment screening prototype that helps recruiters compare multiple resumes against a job description. Instead of producing only a match percentage, it provides an **explainable candidate profile** with matched skills, skill gaps, weighted score, ranking and recommendation.

## 🚀 Key Features

- Upload multiple PDF/DOCX resumes
- Enter a target job description
- Automatic skill extraction
- Required-skill matching
- Explainable weighted candidate score
- Candidate ranking
- Skill-gap analysis
- Recommendation: Highly Recommended / Consider / Low Match
- Download ranking as CSV
- Clean Streamlit dashboard

## 🧠 Approach

**Job Description + Resumes → Text Extraction → Skill Detection → Skill/Keyword Matching → Weighted Scoring → Ranking → Explanation**

The prototype uses transparent NLP-style processing and weighted scoring so that the result can be explained during a practical/viva.

### Scoring Logic

- 55% — required skill coverage
- 30% — textual relevance between resume and job description
- 15% — project/experience signal

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- PDFPlumber
- DOCX2TXT
- Regular-expression based NLP preprocessing

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## 📁 Project Structure

```text
TalentLens-AI/
├── app.py
├── analyzer.py
├── matcher.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── sample_resumes/
├── screenshots/
└── .gitignore
```

## ⚠️ Responsible AI Note

TalentLens AI is a decision-support prototype. It should not be used as an autonomous hiring decision-maker. Real recruitment systems should be evaluated for fairness, bias, privacy, security and compliance before deployment.
