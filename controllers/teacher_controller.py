"""Teacher controller with all its routes"""
from sqlite3 import Error
from flask import Blueprint, session, render_template, redirect, url_for, request
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
    """Teachers route which shows all the teachers from the database"""
    if session["is_admin"] == 1:
        teacher_model = TeacherModel(DATABASE_FILE)
        username = session["user"]
        select_teachers = teacher_model.get_all_teachers()

        return render_template(
            "teacher/teachers.html.j2", teachers=select_teachers, username=username
        )
    return redirect(url_for("dashboard"))


@teachers_page.route("/create_teacher", methods=["GET", "POST"])
def create_teacher():
    """Create teacher route that creates a teacher and inserts it into the database"""
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
        return render_template(
            "teacher/create_teacher.html.j2", username=username, form=teacher_form
        )
    return redirect(url_for("dashboard"))


@teachers_page.route("/delete_teacher", methods=["GET", "POST"])
def delete_teacher():
    """Delete teacher route that deletes a specific teacher from the database"""
    if session["is_admin"] == 1:
        teacher_model = TeacherModel(DATABASE_FILE)
        if request.method == "POST":
            try:
                teacher_id = request.form["teacher_id"]
                teacher_model.delete_teacher(teacher_id=teacher_id)

            except Error as error:
                print(error)

        return redirect(url_for("teachers.teachers"))

    return redirect(url_for("dashboard"))


@teachers_page.route("/search_teacher", methods=["GET", "POST"])
def search_teacher():
    """Searches for a specific teacher if the search value aligns with their name or username and
    selects them from the database"""
    if session["is_admin"] == 1:
        result = None
        teacher_model = TeacherModel(DATABASE_FILE)
        username = session["user"]
        select_teachers = teacher_model.get_all_teachers()
        if request.method == "POST":
            try:
                search_value = request.form["search_value"]

                result = teacher_model.search_teacher(search_value=search_value)
            except Error as error:
                print(error)

        return render_template(
            "teacher/teachers.html.j2",
            result=result,
            teachers=select_teachers,
            username=username,
        )
    return redirect(url_for("login"))


@teachers_page.route("/edit_teacher", methods=["POST", "GET"])
def edit_teacher():
    """Edit teacher route that edits the changed fields from the teacher into the database"""
    if session["is_admin"] == 1:
        bcrypt = Bcrypt()
        teacher_model = TeacherModel(DATABASE_FILE)
        if request.method == "POST":
            try:
                display_name = request.form["display_name"]
                username = request.form["username"]
                teacher_password = request.form["teacher_password"]
                is_admin = request.form["is_admin"]
                teacher_id = request.form["teacher_id"]
                hashed_password = bcrypt.generate_password_hash(teacher_password)
                teacher_model.update_teacher(
                    display_name=display_name,
                    username=username,
                    teacher_password=hashed_password,
                    is_admin=is_admin,
                    teacher_id=teacher_id,
                )
            except Error as error:
                print(error)

        return redirect(url_for("teachers.teachers"))

    return redirect(url_for("login"))


@teachers_page.route("/profile", methods=["GET", "POST"])
def profile():
    if "user" in session:
        admin = session["is_admin"]
        display_name = session["display_name"]
        username = session["user"]

        return render_template(
            "teacher/profile.html.j2",
            display_name=display_name,
            username=username,
            admin=admin,
        )


@teachers_page.route("/teacher/<int:teacher_id>", methods=["POST", "GET"])
def teacher(teacher_id):
    if session["is_admin"] == 1:
        selected_teacher = None
        teacher_model = TeacherModel(DATABASE_FILE)
        username = session["user"]
        if request.method == "POST":
            try:
                teacher_id = request.form["teacher_id"]
                selected_teacher = teacher_model.select_teacher(teacher_id=teacher_id)
            except Error as error:
                print(error)
        return render_template(
            "teacher/teacher.html.j2",
            teacher=selected_teacher,
            teacher_id=teacher_id,
            username=username,
        )

    return redirect(url_for("login"))
