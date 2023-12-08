from flask import Blueprint, session, render_template, redirect, url_for

from controllers.questions_controller import QuestionsController

questions_page = Blueprint("questions", __name__, url_prefix="/questions", template_folder="templates/question",
                           static_folder="static")

@questions_page.route("/", methods=["GET", "POST"])
def questions():
    if "user" in session:
        username = session["user"]
        question_controller = QuestionsController()
        questions = question_controller.select_questions()

        return render_template("question/questions.html.j2", questions=questions, username=username)
    else:
        redirect(url_for("login"))
