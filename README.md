# 🧠 AI Career Digital Twin System

An AI-powered Career Digital Twin web application built using **Python, Flask, Machine Learning, and Scikit-learn**. The system analyzes a user's profile, predicts the most suitable career role, identifies skill gaps, calculates a career readiness score, provides salary insights, and generates a personalized learning roadmap.

---

# 📌 Project Overview

The AI Career Digital Twin System creates a virtual representation of a user's career profile by analyzing their skills, experience, and career interests. It uses Machine Learning to recommend suitable career roles and provides actionable insights to help users improve their employability.

---

# ✨ Features

- 👤 User Profile Management
  - Name
  - Email
  - Age
  - Fresher / Experienced
  - Years of Experience

- 💻 Skills Analysis

- 🎯 Career Role Prediction using Machine Learning

- 📊 Career Readiness Score (0–100)

- ⚠️ Skill Gap Analysis

- 📚 Personalized Learning Roadmap

- 💰 Salary Insights

- 🎨 Responsive Bootstrap Dashboard

- 🤖 AI-Based Career Recommendation Engine

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Flask | Web Framework |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning |
| CountVectorizer | Text Feature Extraction |
| Naive Bayes | Career Prediction Model |
| HTML | User Interface |
| Bootstrap 5 | Dashboard Design |
| CSS | Styling |

---

# 📂 Project Structure

```text
ai-career-twin/
│
├── app.py
├── model.py
├── data.csv
├── requirements.txt
├── README.md
├── architecture.png
│
└── screenshots/
      ├── home.png
      └── result.png
```

---

# 🏗️ System Architecture

![Architecture](architecture.png)

---

# 🔄 Workflow

1. User enters personal information.
2. User enters skills and preferred career role.
3. Flask receives user input.
4. Machine Learning model processes the skills.
5. AI predicts the most suitable career role.
6. System calculates career readiness score.
7. Skill gaps are identified.
8. Learning roadmap is generated.
9. Salary insights are displayed.
10. Results are shown on the dashboard.

---

# 🧠 Machine Learning Model

### Algorithm Used

- Multinomial Naive Bayes Classifier

### Feature Extraction

- CountVectorizer

### Dataset

A custom dataset containing:

- Skills
- Career Roles

Example:

| Skills | Role |
|---------|------|
| python sql | Data Analyst |
| python ml | Data Scientist |
| html css javascript | Frontend Developer |

---

# 📊 Output Generated

The system provides:

- ✅ Predicted Career Role
- ✅ Career Readiness Score
- ✅ Skill Gap Analysis
- ✅ Learning Roadmap
- ✅ Salary Insight
- ✅ Personalized Recommendations

---

# 📸 Screenshots

## Home Page

![Home](screenshots/home.png)

---

## Result Dashboard

![Result](screenshots/result.png)

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-career-digital-twin.git
```

---

## Open Project

```bash
cd ai-career-digital-twin
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

---

## Open Browser

```
http://127.0.0.1:5000
```

---

# 🎯 Example Input

**Name**

```
Shrusti
```

**Skills**

```
python sql excel
```

**Interested Role**

```
Data Analyst
```

---

# 📈 Example Output

- Predicted Role: Data Analyst
- Career Score: 85/100
- Missing Skills: Power BI
- Salary: ₹3–6 LPA
- Roadmap:
  - Learn SQL
  - Learn Power BI
  - Build Data Analysis Projects

---

# 🚀 Future Enhancements

- Resume Upload (PDF/DOCX)
- Resume Parsing using NLP
- AI Career Chatbot
- Login & Authentication
- User Database (SQLite/MySQL)
- Dashboard Analytics
- Career Trend Prediction
- Job Recommendation API Integration
- Certificate Recommendation System
- PDF Career Report Generator
- Email Report Generation
- Cloud Deployment (Render/AWS/Azure)

---

# 🎓 Learning Outcomes

This project demonstrates knowledge of:

- Machine Learning
- Natural Language Processing (Basic)
- Flask Web Development
- Data Processing
- Feature Engineering
- Career Recommendation Systems
- Bootstrap UI Development
- End-to-End AI Application Development

---

# 👩‍💻 Author

**Shrusti M**

AI Career Digital Twin System

Built using Python, Flask, Machine Learning, and Bootstrap.

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub!