from flask import Blueprint, session, render_template, redirect, url_for
from flask_bcrypt import Bcrypt
from controllers.teacher_controller import TeacherController
from views.forms.teacher_form import TeacherForm


teachers_page = Blueprint("teachers", __name__, url_prefix="/teachers", template_folder="templates/teacher", static_folder="static")


@teachers_page.route("/", methods=["GET", "POST"])
def teachers():
    if session["is_admin"] == 1:
        teacher_controller = TeacherController()
        username = session["user"]
        teachers = teacher_controller.select_teachers()

        return render_template("teacher/teachers.html.j2", teachers=teachers, username=username)
    else:
        return redirect(url_for("dashboard"))


@teachers_page.route("/create_teacher", methods=["GET", "POST"])
def create_teacher():
    if session["is_admin"] == 1:
        teacher_controller = TeacherController()
        teacher_form = TeacherForm()
        bcrypt = Bcrypt()
        username = session["user"]
        if teacher_form.validate_on_submit():
            display_name = teacher_form.display_name.data
            username = teacher_form.username.data
            teacher_password = teacher_form.teacher_password.data
            is_admin = teacher_form.is_admin.data

            hashed_password = bcrypt.generate_password_hash(teacher_password)

            teacher_controller.insert_teacher(display_name=display_name, username=username, teacher_password=hashed_password, is_admin=is_admin)

            return redirect(url_for("teachers.teachers"))
        else:
            print(teacher_form.errors)
        return render_template("teacher/create_teacher.html.j2", username=username, form=teacher_form)
    else:
        return redirect(url_for("dashboard"))


