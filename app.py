import streamlit as st
import PyPDF2
import requests

# ===== Page Config =====
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("AI Resume Analyzer (LLM Powered)")
st.write("Upload your resume and paste a job description to get ATS insights.")

# ===== API Key from Streamlit Secrets =====
try:
    OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]
except:
    st.error("API key not found. Please add it in .streamlit/secrets.toml")
    st.stop()

# ===== File Upload =====
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

# ===== Job Description =====
jd_text = st.text_area("Paste Job Description", height=200)

# ===== Extract Text from PDF =====
def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

# ===== OpenRouter Function =====
def analyze_with_llm(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# ===== Analyze Button =====
if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.warning("Please upload a resume.")
    
    elif jd_text.strip() == "":
        st.warning("Please paste a job description.")
    
    else:
        with st.spinner("Analyzing with AI..."):
            try:
                resume_text = extract_text(uploaded_file)

                prompt = f"""
You are an ATS system.

Compare the resume with the job description.

Provide:
1. ATS Match Score (0-100)
2. Strengths
3. Missing Skills
4. Suggestions to improve the resume

Resume:
{resume_text}

Job Description:
{jd_text}
"""

                result = analyze_with_llm(prompt)

                st.subheader("Analysis Result")
                st.write(result)

            except Exception as e:
                st.error(f"Error: {e}")
