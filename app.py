import streamlit as st
import pandas as pd
from pathlib import Path
from analyzer import extract_text, analyze_resume
from matcher import rank_candidates

st.set_page_config(page_title="TalentLens AI", page_icon="🎯", layout="wide")

st.markdown("""
<style>
.main {padding-top: 1.5rem;}
.hero {padding: 1.5rem 1.8rem; border-radius: 18px; background: linear-gradient(135deg,#111827,#312e81); color:white; margin-bottom:1.5rem;}
.hero h1 {margin:0; font-size:2.2rem;}
.hero p {margin:.4rem 0 0; color:#dbeafe;}
.card {padding:1rem; border-radius:14px; background:#f8fafc; border:1px solid #e5e7eb;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🎯 TalentLens AI</h1>
<p>Explainable AI-based Resume Screening, Skill Gap Analysis & Candidate Ranking</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Screening Setup")
    st.caption("Enter the role requirements and upload candidate resumes.")
    job_title = st.text_input("Job Title", "Python Developer")
    jd = st.text_area(
        "Job Description",
        "We are looking for a Python Developer with Python, SQL, Machine Learning, Flask, Git and REST API skills. Candidates should have strong problem-solving ability and relevant projects.",
        height=190
    )
    threshold = st.slider("Strong Match Threshold", 60, 90, 75)

uploads = st.file_uploader(
    "📄 Upload candidate resumes (PDF or DOCX)",
    type=["pdf","docx"],
    accept_multiple_files=True
)

if not uploads:
    st.info("Upload at least one resume to start screening.")
    st.markdown("### How it works")
    cols = st.columns(4)
    for c, title, text in zip(cols,
        ["1. Parse","2. Understand","3. Rank","4. Explain"],
        ["Extract resume text","Identify skills & signals","Calculate weighted scores","Show strengths & skill gaps"]):
        c.markdown(f"<div class='card'><b>{title}</b><br>{text}</div>", unsafe_allow_html=True)
    st.stop()

candidates = []
errors = []
for file in uploads:
    try:
        text = extract_text(file)
        if len(text.strip()) < 40:
            errors.append(f"{file.name}: not enough readable text.")
            continue
        candidates.append(analyze_resume(file.name, text, jd))
    except Exception as e:
        errors.append(f"{file.name}: {e}")

if errors:
    for e in errors:
        st.warning(e)

if not candidates:
    st.error("No readable resumes were found.")
    st.stop()

results = rank_candidates(candidates, jd)
df = pd.DataFrame([{
    "Rank": i + 1,
    "Candidate": r["candidate"],
    "Match Score": r["score"],
    "Skills Matched": len(r["matched_skills"]),
    "Skills Missing": len(r["missing_skills"]),
    "Recommendation": r["recommendation"]
} for i, r in enumerate(results)])

st.subheader(f"📊 Candidate Ranking — {job_title}")
st.dataframe(df, use_container_width=True, hide_index=True)

st.download_button(
    "⬇️ Download Ranking CSV",
    df.to_csv(index=False).encode("utf-8"),
    "talentlens_ranking.csv",
    "text/csv"
)

st.subheader("🔎 Explainable Candidate Analysis")
for i, r in enumerate(results):
    label = f"#{i+1}  {r['candidate']} — {r['score']}/100"
    with st.expander(label, expanded=(i == 0)):
        a,b,c,d = st.columns(4)
        a.metric("Overall Match", f"{r['score']}/100")
        b.metric("Skill Match", f"{r['skill_score']}/100")
        c.metric("Project/Relevance", f"{r['relevance_score']}/100")
        d.metric("Keyword Coverage", f"{r['keyword_score']}%")

        st.markdown("**Why this candidate?**")
        st.write(r["explanation"])

        left,right = st.columns(2)
        with left:
            st.markdown("**✅ Matched Skills**")
            st.write(", ".join(r["matched_skills"]) if r["matched_skills"] else "None detected")
        with right:
            st.markdown("**❌ Skill Gaps**")
            st.write(", ".join(r["missing_skills"]) if r["missing_skills"] else "No major skill gaps detected")

        st.markdown(f"**Recommendation:** {r['recommendation']}")
        st.progress(r["score"]/100)

st.caption("TalentLens AI uses transparent NLP-based matching and weighted scoring to support recruiter decisions. It is a decision-support prototype, not an autonomous hiring system.")
