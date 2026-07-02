from flask import Flask, request, render_template_string
from model import predict_role

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Career Digital Twin</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">

<div class="container mt-5">

    <div class="text-center mb-4">
        <h1>🧠 AI Career Digital Twin</h1>
        <p class="text-muted">Analyze your career like a real AI system</p>
    </div>

    <div class="card p-4 shadow">

        <form method="POST">

            <div class="row">
                <div class="col">
                    <input class="form-control" name="name" placeholder="Name" required>
                </div>
                <div class="col">
                    <input class="form-control" name="email" placeholder="Email" required>
                </div>
                <div class="col">
                    <input class="form-control" name="age" type="number" placeholder="Age" required>
                </div>
            </div>

            <br>

            <div class="row">
                <div class="col">
                    <select class="form-control" name="experience_type">
                        <option value="fresher">Fresher</option>
                        <option value="experienced">Experienced</option>
                    </select>
                </div>

                <div class="col">
                    <input class="form-control" name="years_exp" type="number" placeholder="Years Experience">
                </div>

                <div class="col">
                    <input class="form-control" name="salary" placeholder="Expected Salary (LPA)">
                </div>
            </div>

            <br>

            <input class="form-control" name="skills" placeholder="Skills (python sql excel)" required>
            <br>

            <input class="form-control" name="interest" placeholder="Interested Role">
            <br>

            <button class="btn btn-primary w-100">Analyze Career</button>

        </form>
    </div>

    {% if result %}

    <div class="mt-4">

        <div class="card p-3 shadow">
            <h4>👤 User: {{ result.name }}</h4>
            <p><b>Predicted Role:</b> {{ result.role }}</p>
        </div>

        <br>

        <div class="card p-3 shadow">
            <h4>🎯 Career Score</h4>
            <h2>{{ result.score }}/100</h2>
            <p>{{ result.level }}</p>
        </div>

        <br>

        <div class="card p-3 shadow">
            <h4>⚠ Skill Gap</h4>
            <p>{{ result.gap }}</p>
        </div>

        <br>

        <div class="card p-3 shadow">
            <h4>📚 Learning Roadmap</h4>
            <p>{{ result.roadmap }}</p>
        </div>

        <br>

        <div class="card p-3 shadow">
            <h4>💰 Salary Insight</h4>
            <p>{{ result.salary }}</p>
        </div>

    </div>

    {% endif %}

</div>

</body>
</html>
"""

# role-based knowledge
role_data = {
    "data analyst": {
        "skills": ["excel", "sql", "powerbi", "python"],
        "salary": "3 - 6 LPA",
        "roadmap": "Learn Excel → SQL → Power BI → Python"
    },
    "data scientist": {
        "skills": ["python", "ml", "statistics", "pandas"],
        "salary": "6 - 15 LPA",
        "roadmap": "Python → Statistics → ML → Deep Learning"
    },
    "backend developer": {
        "skills": ["java", "spring", "nodejs", "sql"],
        "salary": "5 - 12 LPA",
        "roadmap": "Java → APIs → Databases → Spring Boot"
    },
    "frontend developer": {
        "skills": ["html", "css", "javascript", "react"],
        "salary": "4 - 10 LPA",
        "roadmap": "HTML → CSS → JS → React"
    }
}

def calculate_score(user_skills, role_skills):
    user_skills = user_skills.lower().split()
    match = 0

    for s in user_skills:
        if s in role_skills:
            match += 25

    return min(match, 100)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":

        name = request.form["name"]
        skills = request.form["skills"]
        interest = request.form["interest"]

        role = predict_role(skills)

        data = role_data.get(role, {
            "skills": [],
            "salary": "Not Available",
            "roadmap": "No roadmap available"
        })

        score = calculate_score(skills, data["skills"])

        level = "Beginner"
        if score > 70:
            level = "Job Ready"
        elif score > 40:
            level = "Intermediate"

        gap = list(set(data["skills"]) - set(skills.lower().split()))
        gap_text = ", ".join(gap) if gap else "No major gaps"

        result = {
            "name": name,
            "role": role,
            "score": score,
            "level": level,
            "gap": gap_text,
            "roadmap": data["roadmap"],
            "salary": data["salary"]
        }

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)