import streamlit as st
from resume_parser import extract_text
from utils import clean_text
from skill_matcher import extract_skills, calculate_similarity

st.title("AI Based ATS Resume Matcher")

resume_file = st.file_uploader("Upload Resume (PDF or DOCX)")
jd_text = st.text_area("Paste Job Description Here")

if st.button("Analyze Resume"):

    if resume_file and jd_text:

        resume_text = extract_text(resume_file)

        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(jd_text)

        resume_skills = extract_skills(resume_clean)
        jd_skills = extract_skills(jd_clean)

        score = calculate_similarity(resume_clean, jd_clean)

        st.subheader("Match Score")
        st.write(f"{score} %")

        st.subheader("Matched Skills")
        st.write(list(set(resume_skills).intersection(set(jd_skills))))

        st.subheader("Missing Skills")
        st.write(list(set(jd_skills) - set(resume_skills)))

    else:
        st.warning("Please upload resume and paste job description")
