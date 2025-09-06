import pdfplumber
import re
import json

# -------------------------
# Extract text from PDF

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


# -------------------------
# Extract contact info

def extract_contact_info(text):
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\+?\d[\d\s-]{8,}\d', text)
    return email, phone


# -------------------------
# Extract skills

skills_db = ["python", "java", "aws", "machine learning", "sql", "django", "flask"]

def extract_skills(text):
    found = []
    for skill in skills_db:
        if skill.lower() in text.lower():
            found.append(skill)
    return list(set(found))  # remove duplicates


# -------------------------
# Save results as JSON

def save_to_json(data, filename="parsed_resume.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Results saved to {filename}")



if __name__ == "__main__":
    resume_file = r'E:\Python practice\Resume Parser\DarshanM-Resume.pdf'

    print("🔍 Parsing resume:", resume_file)
    text = extract_text_from_pdf(resume_file)

    email, phone = extract_contact_info(text)
    skills = extract_skills(text)

    parsed_data = {
        "email": email,
        "phone": phone,
        "skills": skills
    }

    save_to_json(parsed_data)
    print(" Parsed Data:", parsed_data)
