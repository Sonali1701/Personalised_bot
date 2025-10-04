import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import PyPDF2

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")

# Function to extract text from a local PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# Function to ask Gemini a question
def ask_gemini(question, profile_text):
    prompt = f"""
    You are answering questions based only on the recruiter profile below:

    --- PROFILE START ---
    {profile_text}
    --- PROFILE END ---

    Question: {question}
    """
    response = model.generate_content(prompt)
    return response.text

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Recruiter Q&A Bot", page_icon="🤖", layout="centered")
st.title("🤖 Recruiter Q&A Bot (Powered by Gemini)")
st.write("Ask personalized questions about the Kunal Kapur.")

# 🔹 Preload recruiter PDF once (change filename here)
PROFILE_PATH = "recruiter.pdf"
profile_text = extract_text_from_pdf(PROFILE_PATH)

# Show auto-summary
if st.button("Generate Profile Summary"):
    with st.spinner("Summarizing profile..."):
        summary = ask_gemini("Summarize this recruiter's profile in 3-4 sentences.", profile_text)
        st.subheader("📋 Recruiter Summary")
        st.write(summary)

# Ask questions
question = st.text_input("Ask a question about the Kunal Kapur:")
if st.button("Get Answer"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = ask_gemini(question, profile_text)
            st.subheader("✨ Answer")
            st.write(answer)
    else:
        st.warning("Please enter a question.")
