from flask import Blueprint, session, render_template, redirect, url_for

from controllers.teacher_controller import TeacherController

teachers_page = Blueprint("teachers", __name__, url_prefix="/teachers", template_folder="templates/teacher", static_folder="static")

teacher_controller = TeacherController()


@teachers_page.route("/", methods=["GET", "POST"])
def teachers():
    if session["is_admin"] == 1:
        teachers = teacher_controller.select_teachers()

        return render_template("teacher/teachers.html.j2", teachers=teachers)
    else:
        return redirect(url_for("dashboard"))