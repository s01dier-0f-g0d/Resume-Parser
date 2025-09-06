# Resume-Parser
# 📄 Resume Parser (Python)

A simple Resume Parser built with Python.
This script extracts text from a resume (PDF), finds email, phone numbers, and skills, and saves the structured results into a JSON file.

# 🚀 Features

Extracts text from PDF resumes

Finds Email and Phone numbers using Regex

Matches Skills against a predefined skills database

Saves results as a structured JSON file

# 🛠️ Requirements

Python 3.8+

Install dependencies:

pip install pdfplumber

# 📂 Project Structure
resume-parser/
│── main1.py   # Main script
│── resume.pdf         # Sample resume (replace with your own)
│── parsed_resume.json # Output file
└── README.md

# ▶️ How to Run

Clone or download the repository.

Place your resume PDF in the same folder as the script (e.g., resume.pdf).

Run the script:

python main1.py


Check the results in:

Console output

parsed_resume.json file

# 📊 Example Output
{
    "email": ["john.doe@email.com"],
    "phone": ["+1 234 567 8901"],
    "skills": ["Python", "SQL", "AWS"]
}

