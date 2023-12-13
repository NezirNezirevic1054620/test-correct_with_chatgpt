from flask import Blueprint, session, render_template, redirect, url_for, request
from sqlite3 import Error
from flask_bcrypt import Bcrypt
from models.teacher_model import TeacherModel
from forms.teacher_form import TeacherForm

teachers_page = Blueprint(
    "teachers",
    __name__,
    url_prefix="/teachers",
    template_folder="templates/teacher",
    static_folder="static",
)

DATABASE_FILE = "databases/testgpt.db"


@teachers_page.route("/", methods=["GET", "POST"])
def teachers():
    if session["is_admin"] == 1:
        teacher_model = TeacherModel(DATABASE_FILE)
        username = session["user"]
        select_teachers = teacher_model.get_all_teachers()

        return render_template(
            "teacher/teachers.html.j2", teachers=select_teachers, username=username
        )
    else:
        return redirect(url_for("dashboard"))


@teachers_page.route("/create_teacher", methods=["GET", "POST"])
def create_teacher():
    if session["is_admin"] == 1:
        teacher_model = TeacherModel(DATABASE_FILE)
        teacher_form = TeacherForm()
        bcrypt = Bcrypt()
        username = session["user"]
        if teacher_form.validate_on_submit():
            display_name = teacher_form.display_name.data
            username = teacher_form.username.data
            teacher_password = teacher_form.teacher_password.data
            is_admin = teacher_form.is_admin.data

            hashed_password = bcrypt.generate_password_hash(teacher_password)

            teacher_model.insert_teacher(
                display_name=display_name,
                username=username,
                teacher_password=hashed_password,
                is_admin=is_admin,
            )

            return redirect(url_for("teachers.teachers"))
        else:
            print(teacher_form.errors)
        return render_template(
            "teacher/create_teacher.html.j2", username=username, form=teacher_form
        )
    else:
        return redirect(url_for("dashboard"))


@teachers_page.route("/delete_teacher", methods=["GET", "POST"])
def delete_teacher():
    if "user" in session:
        teacher_model = TeacherModel(DATABASE_FILE)
        if request.method == "POST":
            try:
                teacher_id = request.form["teacher_id"]
                teacher_model.delete_teacher(teacher_id=teacher_id)

            except Error as error:
                print(error)

        return redirect(url_for("teachers.teachers"))
    else:
        return redirect(url_for("dashboard"))
