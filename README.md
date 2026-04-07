# Interview Company Preparation Project 🎯

A Flask-based AI-powered web application that generates a complete **Interview Preparation Roadmap** based on user inputs such as **Role, Programming Language, and Experience**.  
It provides a structured plan including **DSA topics, LeetCode practice questions, aptitude syllabus, CS fundamentals, and role-specific preparation**.

---

## 🚀 Features

✅ User-friendly web interface (HTML Forms)  
✅ Takes input: Role, Language, Experience  
✅ Generates a complete interview roadmap using AI  
✅ Includes:
- DSA Roadmap (Topic-wise)
- Curated LeetCode Questions List
- Most Asked Interview DSA Questions
- Aptitude Topics to Cover
- CS Fundamentals (OS, CN, DBMS, OOP)
- Role-Specific Preparation
- Weekly Preparation Plan

✅ Output is directly displayed on the webpage

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **HTML / Jinja Templates**
- **DeepSeek AI API (Chat Completion Model)**

---

## 📂 Project Structure
Interview-Preparation-Project/
│
├── app.py
├── connection.py
├── templates/
│ ├── input_response.html
│ ├── output_response.html
│
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Interview-Preparation-Project.git
cd Interview-Preparation-Project
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate Virtual Environment:

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
3️⃣ Install Dependencies
pip install flask openai
4️⃣ Configure API Key

⚠️ Do not hardcode your API key inside code.
Instead, set it as an environment variable.

Windows (CMD):
set DEEPSEEK_API_KEY=your_api_key_here
Windows (PowerShell):
$env:DEEPSEEK_API_KEY="your_api_key_here"
Mac/Linux:
export DEEPSEEK_API_KEY="your_api_key_here"

Then update your connection.py like:

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
▶️ Run the Application
python app.py

Then open in browser:

http://127.0.0.1:5000/
🖥️ How It Works
User enters:
Role (Backend Developer, Frontend Developer, etc.)
Programming Language (Java, Python, etc.)
Experience (0, 1, 2, 3+ years)
The AI generates a personalized interview roadmap.
Output is shown on the result page.
📌 Example Input
Role: Backend Developer
Language: Java
Experience: 0 years
📌 Example Output Includes
DSA topics roadmap
Best LeetCode questions for practice
Aptitude syllabus (Quant, LR, Verbal)
CS fundamentals list (DBMS, OS, CN, OOP)
Weekly plan for preparation
🔐 Security Note

Try it out:
https://athurj.pythonanywhere.com/


👨‍💻 Author

Atharva Joshi
AI + Flask Project for Interview Preparation
