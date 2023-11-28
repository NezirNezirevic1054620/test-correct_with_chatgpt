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


@notes_page.route("/select_note", methods=["POST", "GET"])
def select_note():
    select_categories = CategoriesController.select_categories()
    select_teachers = TeacherController.select_teachers()
    if request.method == "POST":
        try:
            note_id = request.form["note_id"]
            note = notes_controller.select_note(note_id=note_id)
            print(note)
        except Error as error:
            print(error)
    return render_template("note.html.j2", note=note, teachers=select_teachers, categories=select_categories)


@notes_page.route("/edit_note", methods=["POST", "GET"])
def edit_note():
    if request.method == "POST":
        try:
            title = request.form["title"]
            note_source = request.form["note_source"]
            is_public = request.form["is_public"]
            teacher_id = request.form["teacher_id"]
            category_id = request.form["category_id"]
            note_id = request.form["note_id"]
            note = request.form["note"]
            print(teacher_id)
            notes_controller.edit_note(title=title, note_source=note_source, is_public=is_public,
                                       teacher_id=teacher_id, category_id=category_id, note=note, note_id=note_id)
        except Error as error:
            print(error)

    return redirect(url_for('notes.notes'))


@notes_page.route("/search_note", methods=["POST", "GET"])
def search_note():
    note = 0
    if request.method == "POST":
        try:
            search_value = request.form["search_value"]
            note = notes_controller.search_note(search_value=search_value)
            print(note)
        except Error as error:
            print(error)

    return render_template("search_note.html.j2", result=note)


@notes_page.route("/notes")
def notes():
    select_notes = NotesController.select_notes()
    return render_template("notes.html.j2", notes=select_notes)
