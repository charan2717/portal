from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = "submissions.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
@app.route("/recruit")
def recruit():
    return render_template("recruit.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = load_data()
    form_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "role": request.form["role"],
        "skills": request.form["skills"],
        "linkedin": request.form["linkedin"],
    }
    data.append(form_data)
    save_data(data)
    return render_template("thank_you.html")

@app.route("/admin")
def admin():
    data = load_data()
    return render_template("admin.html", submissions=data)

if __name__ == "__main__":
    app.run(debug=True)
