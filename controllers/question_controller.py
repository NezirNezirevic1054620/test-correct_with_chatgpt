from flask import Blueprint, session, render_template, redirect, url_for, Response, request
from sqlite3 import Error

from models.question_model import QuestionModel
import csv
from io import StringIO

questions_page = Blueprint(
    "questions",
    __name__,
    url_prefix="/questions",
    template_folder="templates/question",
    static_folder="static",
)

DATABASE_FILE = "databases/testgpt.db"


@questions_page.route("/", methods=["GET", "POST"])
def questions():
    if "user" in session:
        username = session["user"]
        question_controller = QuestionModel(DATABASE_FILE)
        get_questions = question_controller.get_all_questions()

        return render_template(
            "question/questions.html.j2", questions=get_questions, username=username
        )
    else:
        redirect(url_for("login"))



@questions_page.route("/delete_questions", methods=["GET", "POST"])
def delete_question():
    if "user" in session:
        question_model = QuestionModel(DATABASE_FILE)
        if request.method == "POST":
            try:
                questions_id = request.form["questions_id"]
                question_model.delete_question(questions_id=questions_id)

            except Error as error:
                print(error)

        return redirect(url_for("questions.questions"))
    else:
        return redirect(url_for("login"))



@questions_page.route("/generate_csv", methods=["POST"])
def generate_csv():
    question_controller = QuestionModel(DATABASE_FILE)
    select_questions = question_controller.get_all_questions()

    csv_data = StringIO()
    csv_writer = csv.writer(csv_data)
    csv_writer.writerow(["Note", "Question", "Created at"])

    for question_row in select_questions:
        csv_writer.writerow(
            [
                question_row["note"],
                question_row["exam_question"],
                question_row["date_created"],
            ]
        )

    response = Response(csv_data.getvalue(), content_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=exam_questions.csv"

    return response
