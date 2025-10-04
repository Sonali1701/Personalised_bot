# Personalised Q&A Bot (Powered by Google Gemini)

## Overview  
This project was built as part of the **Intern Assignment – Build a Tiny AI-Powered App**.  
It’s an **AI-powered Recruiter Q&A Bot** that uses **Google Gemini** to read a recruiter’s LinkedIn profile (PDF) and answer questions about their experience, skills, or background.

The idea behind this project is to go **beyond a simple chatbot** — it’s a personalized app that analyzes a recruiter’s profile and gives intelligent answers instantly.

---

## Features

- Reads and understands a recruiter's LinkedIn PDF profile  
- Lets users ask natural questions (e.g., *“What industry does this recruiter work in?”*)  
- Automatically summarizes the recruiter’s profile  
- Built using **Python + Streamlit + Google Gemini API**  
- API keys secured using `.env` and `.gitignore`  
- Fully deployable on **Streamlit Cloud**

---

## Tech Stack

| Tool / Library | Purpose |
|-----------------|----------|
| **Python 3** | Core programming language |
| **Streamlit** | UI for the web app |
| **Google Generative AI (Gemini)** | Q&A and text generation |
| **PyPDF2** | Extract text from LinkedIn PDF |
| **python-dotenv** | Handle environment variables securely |

---

## Setup Instructions

### 1️. Clone the Repository
```bash
git clone https://github.com/<your-username>/Recruiter-QA-Bot.git
cd Recruiter-QA-Bot
```

### 2.Create a Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate    # On Windows
source .venv/bin/activate # On Mac/Linux
```

### 3.Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️.Add Your API Key

Create a .env file in your project folder:
```bash

GEMINI_API_KEY=your_api_key_here
```

### 5.Run the App Locally
```bash
streamlit run app.py
```
