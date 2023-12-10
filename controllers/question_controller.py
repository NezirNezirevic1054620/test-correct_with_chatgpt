from flask import Blueprint, session, render_template, redirect, url_for

from models.question_model import QuestionModel

questions_page = Blueprint("questions", __name__, url_prefix="/questions", template_folder="templates/question",
                           static_folder="static")

DATABASE_FILE = "databases/testgpt.db"


@questions_page.route("/", methods=["GET", "POST"])
def questions():
    if "user" in session:
        username = session["user"]
        question_controller = QuestionModel(DATABASE_FILE)
        get_questions = question_controller.get_all_questions()

        return render_template("question/questions.html.j2", questions=get_questions, username=username)
    else:
        redirect(url_for("login"))
