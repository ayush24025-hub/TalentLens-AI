# TalentLens AI — Project Report

## 1. Introduction
Recruiters often receive many resumes for a single job opening. Manually reviewing each resume can be time-consuming and inconsistent. TalentLens AI is designed as an explainable resume screening and candidate ranking prototype.

## 2. Problem Statement
Build a system that can compare candidate resumes with a job description, identify relevant skills, highlight skill gaps and rank candidates using a transparent scoring method.

## 3. Objectives
1. Reduce repetitive manual resume screening.
2. Identify relevant candidate skills.
3. Compare resumes with job requirements.
4. Highlight missing skills.
5. Produce an understandable candidate ranking.
6. Provide an explainable recommendation rather than a black-box result.

## 4. Proposed Solution
The application accepts a job description and multiple PDF/DOCX resumes. It extracts text, detects skills, calculates skill coverage and textual relevance, applies weighted scoring and ranks candidates.

## 5. Methodology
1. Resume text extraction.
2. Text normalization.
3. Skill identification.
4. Required-skill matching.
5. Skill-gap calculation.
6. Relevance and project/experience signal calculation.
7. Weighted score generation.
8. Candidate ranking and explanation.

## 6. Technologies
Python, Streamlit, Pandas, PDFPlumber, DOCX2TXT and regular-expression based NLP processing.

## 7. Expected Output
The system displays:
- Candidate rank
- Overall match score
- Skill match score
- Matched skills
- Missing skills
- Recommendation
- Explanation

## 8. Advantages
- Fast screening of multiple resumes.
- Transparent scoring.
- Easy-to-understand output.
- Simple local deployment.
- Useful as a recruiter decision-support prototype.

## 9. Limitations
- Skill dictionary is currently predefined.
- Text-based matching may miss context and synonyms.
- It is not a production hiring system.
- Bias and fairness require dedicated evaluation for real-world deployment.

## 10. Future Scope
- Transformer-based semantic embeddings.
- Larger skill ontology.
- Bias/fairness auditing.
- Secure database integration.
- Recruiter feedback loop.
- Role-specific scoring models.

## 11. Conclusion
TalentLens AI demonstrates how NLP-based text processing and explainable scoring can assist the initial stage of resume screening. The project focuses on transparency by showing not only the candidate score but also the reasons, matched skills and skill gaps behind the ranking.
