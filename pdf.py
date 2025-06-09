import fitz  # PyMuPDF
from docx import Document
import re
import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Configure Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Extract text from PDF or TXT
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        return "".join([page.get_text() for page in doc])
    else:
        return uploaded_file.read().decode("utf-8")

# Extract keywords from JD
def extract_keywords(text, top_n=15):
    words = re.findall(r'\b\w+\b', text.lower())
    ignore = set(['and', 'with', 'the', 'for', 'you', 'are', 'that', 'have', 'job', 'your', 'will'])
    freq = {}
    for word in words:
        if len(word) > 3 and word not in ignore:
            freq[word] = freq.get(word, 0) + 1
    sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, count in sorted_keywords[:top_n]]

# Compute keyword match
def keyword_match_score(resume, keywords):
    resume_words = resume.lower()
    match_count = sum(1 for word in keywords if word in resume_words)
    return int((match_count / len(keywords)) * 100)

# Save as DOCX
def save_as_docx(text, filename):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(filename)

# Generate interview questions
def generate_interview_questions(jd_text, resume_text, num_questions=10):
    prompt = f"""
You are an expert career coach.

Based on the following job description and candidate resume, generate {num_questions} likely interview questions that the candidate may face.

Job Description:
{jd_text}

Candidate Resume:
{resume_text}

Provide a numbered list of questions only.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
        contents=prompt
    )
    questions_text = response.text.strip()
    questions_raw = questions_text.split('\n')
    
    # Ensure proper numbering (remove bullets if present)
    cleaned_questions = []
    for i, line in enumerate(questions_raw, start=1):
        if line.strip():
            line = re.sub(r'^\d+[\).\s-]*', '', line).strip()
            cleaned_questions.append(f"{i}. {line}")
    return cleaned_questions

# Streamlit UI Setup
st.set_page_config(page_title="🤖 AI Job Tailor + Interview Prep", layout="wide")
st.title("🤖 Advanced AI Job Application Tailor + Interview Prep")
st.markdown("Upload your resume and job description to generate a tailored resume, cover letter, and likely interview questions.")

col1, col2 = st.columns(2)

# Resume uploader
with col1:
    resume_file = st.file_uploader("📄 Upload Resume (PDF or .txt)", type=["pdf", "txt"])

# JD input
with col2:
    jd_input_mode = st.radio("📋 Job Description Input Mode", ["Upload File", "Type Manually"])
    jd_text = None
    if jd_input_mode == "Upload File":
        jd_file = st.file_uploader("📎 Upload Job Description (PDF or .txt)", type=["pdf", "txt"])
    else:
        jd_text = st.text_area("🖊 Paste or Type the Job Description Here", height=250)
        jd_file = None

# Tone selection
tone = st.selectbox("🗣 Select Writing Tone", ["Formal", "Conversational", "Creative"])

# Generate button
if st.button("🚀 Generate Tailored Documents and Interview Questions"):
    if resume_file and (jd_file or jd_text):
        resume_text = extract_text_from_file(resume_file)
        if jd_file:
            jd_text = extract_text_from_file(jd_file)

        # Keyword match
        keywords = extract_keywords(jd_text)
        match_score = keyword_match_score(resume_text, keywords)

        st.subheader("📊 ATS Keyword Match Score")
        st.progress(match_score / 100)
        st.markdown(f"{match_score}%** match with the job description keywords.")

        with st.spinner("Generating tailored documents and interview questions..."):
            try:
                # Resume + Cover Letter generation
                prompt = f"""
You are a resume and cover letter writing expert.

Task:
- Rewrite the resume to closely match the job description using a {tone.lower()} tone.
- Generate a professional, tailored cover letter for the position.

Job Description:
{jd_text}

Original Resume:
{resume_text}

Output the tailored resume first, then the cover letter. Use markdown headings for separation.
"""
                response = client.models.generate_content(
                    model="gemini-2.5-flash-preview-05-20",
                    contents=prompt
                )

                output_text = response.text.strip()

                # Editable output
                st.subheader("✍ Tailored Resume & Cover Letter")
                editable = st.text_area("Review and edit the generated content if needed:", value=output_text, height=500)

                st.download_button("📄 Download as TXT", editable, file_name="tailored_documents.txt")
                save_as_docx(editable, "tailored_documents.docx")
                with open("tailored_documents.docx", "rb") as f:
                    st.download_button("📄 Download as DOCX", f, file_name="tailored_documents.docx")

                # Interview questions generation
                st.subheader("🎤 Likely Interview Questions")
                questions = generate_interview_questions(jd_text, resume_text)
                for q in questions:
                    st.markdown(q)

            except Exception as e:
                st.error(f"❌ Error during generation: {e}")
    else:
        st.warning("⚠ Please upload both resume and job description.")