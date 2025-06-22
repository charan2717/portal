from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Direct PostgreSQL connection string (for demo purposes only)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://database_b38b_user:5cukegbGC7o0jc3NyrPTF9O69Ao24fb9@dpg-d1bntqadbo4c73c92a10-a/database_b38b"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Submission model
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    skills = db.Column(db.String(200))
    linkedin = db.Column(db.String(200))

# Create tables on first request
@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
@app.route("/recruit")
def recruit():
    return render_template("recruit.html")

@app.route("/submit", methods=["POST"])
def submit():
    submission = Submission(
        name=request.form["name"],
        email=request.form["email"],
        role=request.form["role"],
        skills=request.form["skills"],
        linkedin=request.form["linkedin"]
    )
    db.session.add(submission)
    db.session.commit()
    return render_template("thank_you.html")

@app.route("/admin")
def admin():
    submissions = Submission.query.all()
    return render_template("admin.html", submissions=submissions)

if __name__ == "__main__":
    app.run(debug=True)
