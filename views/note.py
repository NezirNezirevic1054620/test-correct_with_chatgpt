from flask import Blueprint, request, render_template, redirect, url_for
from sqlite3 import Error

from controllers.categories_controller import CategoriesController
from controllers.notes_controller import NotesController
from controllers.teacher_controller import TeacherController

notes_page = Blueprint("notes", __name__, url_prefix="/notes", template_folder="templates", static_folder="static")

notes_controller = NotesController()


@notes_page.route("/create_note", methods=["POST", "GET"])
def create_note():
    select_categories = CategoriesController.select_categories()
    select_teachers = TeacherController.select_teachers()
    if request.method == "POST":
        try:
            title = request.form["title"]
            note_source = request.form["note_source"]
            is_public = request.form["is_public"]
            teacher_id = request.form["teacher_id"]
            category_id = request.form["category_id"]
            note = request.form["note"]

            notes_controller.insert_notes(title=title, note_source=note_source, is_public=is_public,
                                          teacher_id=teacher_id, category_id=category_id, note=note)
            return redirect(url_for('notes.notes'))
        except Error as error:
            print(error)
    return render_template("create_note.html.j2", categories=select_categories, teachers=select_teachers)


@notes_page.route("/delete_note", methods=["GET", "POST"])
def delete_note():
    if request.method == "POST":
        try:
            note_id = request.form["note_id"]
            notes_controller.delete_note(note_id)

        except Error as error:
            print(error)

    return redirect(url_for('notes.notes'))


@notes_page.route("/edit_note", methods=["POST", "GET"])
def edit_note():
    if request.method == "POST":
        try:
            title = request.form["title"]
            note_source = request.form["note_source"]
            is_public = request.form["is_public"]
            teacher_id = request.form["teacher_id"]
            category_id = request.form["category_id"]
            note = request.form["note"]
            notes_controller.edit_note(title=title, note_source=note_source, is_public=is_public,
                                          teacher_id=teacher_id, category_id=category_id, note=note)
        except Error as error:
            print(error)

    return redirect(url_for('notes.notes'))


@notes_page.route("/notes")
def notes():
    select_notes = NotesController.select_notes()
    return render_template("notes.html.j2", notes=select_notes)
