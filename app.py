from flask import Flask, render_template, request, session, redirect, url_for

from controllers.category_controller import category_page
from controllers.note_controller import notes_page
from flask_bcrypt import Bcrypt
from models.category_model import CategoryModel
from models.note_model import NoteModel
from models.question_model import QuestionModel

from models.teacher_model import TeacherModel
from controllers.question_controller import questions_page
from controllers.teacher_controller import teachers_page

import os

SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(notes_page)
app.register_blueprint(category_page)
app.register_blueprint(teachers_page)
app.register_blueprint(questions_page)

DATABASE_FILE = "databases/testgpt.db"


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    teacher_controller = TeacherModel(DATABASE_FILE)
    session.pop("user", None)
    session.pop("teacher_id", None)
    session.pop("is_admin", None)
    session.pop("display_name", None)
    bcrypt = Bcrypt()
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        result = teacher_controller.login(username=username)
        if result:
            if bcrypt.check_password_hash(result[0][3], password):
                session["user"] = username
                session["is_admin"] = result[0][5]
                session["teacher_id"] = result[0][0]
                session["display_name"] = result[0][1]
                return redirect(url_for("dashboard"))
            else:
                return redirect(url_for("login"))

    return render_template("login.html.j2")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" in session:
        teacher_id = session["teacher_id"]
        category_model = CategoryModel(DATABASE_FILE)
        note_model = NoteModel(DATABASE_FILE)
        question_model = QuestionModel(DATABASE_FILE)
        teacher_model = TeacherModel(DATABASE_FILE)
        select_categories = category_model.get_all_categories()
        select_note = note_model.get_all_notes(teacher_id=str(teacher_id))
        select_teacher = teacher_model.get_all_teachers()
        select_question = question_model.get_all_questions()
        counted_categories = len(select_categories)
        counted_note = len(select_note)
        counted_teacher = len(select_teacher)
        counted_question = len(select_question)
        username = session["user"]
        return render_template("beheer.html.j2", username=username, counted_categories=counted_categories,
                               counted_question=counted_question, counted_teacher=counted_teacher,
                               counted_note=counted_note)
    else:
        return redirect(url_for("login"))


@app.route("/admin_dashboard", methods=["GET", "POST"])
def admin_dashboard():
    if "user" in session:
        username = session["user"]
        return render_template("beheer.html.j2", username=username)
    else:
        return redirect(url_for("login"))


app.config["SECRET_KEY"] = SECRET_KEY

if __name__ == "__main__":
    app.run(debug=True)
