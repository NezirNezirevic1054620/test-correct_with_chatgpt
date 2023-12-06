from flask import Blueprint, request, render_template, redirect, url_for, session
from sqlite3 import Error

from controllers.categories_controller import CategoriesController
from controllers.notes_controller import NotesController
from controllers.teacher_controller import TeacherController
from controllers.questions_controller import QuestionsController
from views.forms.note_form import NoteForm
from lib.testgpt.testgpt import TestGPT
import openai
import json

notes_page = Blueprint("notes", __name__, url_prefix="/notes",
                       template_folder="templates/note", static_folder="static")

notes_controller = NotesController()


@notes_page.route("/create_note", methods=["POST", "GET"])
def create_note():
    if "user" in session:
        username = session["user"]
        note_form = NoteForm()
        select_categories = CategoriesController.select_categories()
        select_teachers = TeacherController.select_teachers()
        if note_form.validate_on_submit():
            title = note_form.title.data
            note_source = note_form.note_source.data
            is_public = note_form.is_public.data
            teacher_id = note_form.teacher_id.data
            category_id = note_form.category_id.data
            note_text = note_form.note.data

            notes_controller.insert_notes(title=title, note_source=note_source, is_public=is_public,
                                          teacher_id=teacher_id, category_id=category_id, note=note_text)
            return redirect(url_for('notes.notes'))
        return render_template("note/create_note.html.j2", categories=select_categories, teachers=select_teachers,
                               form=note_form, username=username)
    else:
        return redirect(url_for("login"))


@notes_page.route("/delete_note", methods=["GET", "POST"])
def delete_note():
    if "user" in session:
        if request.method == "POST":
            try:
                note_id = request.form["note_id"]
                notes_controller.delete_note(note_id)

            except Error as error:
                print(error)

        return redirect(url_for('notes.notes'))
    else:
        return redirect(url_for("login"))


@notes_page.route("/note/<int:note_id>", methods=["POST", "GET"])
def note(note_id):
    if "user" in session:
        username = session["user"]
        select_note = None
        select_categories = CategoriesController.select_categories()
        select_teachers = TeacherController.select_teachers()
        if request.method == "POST":
            try:
                note_id = request.form["note_id"]
                select_note = notes_controller.select_note(note_id=note_id)
                select_question = QuestionsController.select_question(
                    note_id=note_id)
                print(select_question)
                print(select_question)
            except Error as error:
                print(error)
        return render_template("note/note.html.j2", note=select_note, teachers=select_teachers,
                               categories=select_categories, note_id=note_id, username=username, question=select_question)
    else:
        return redirect(url_for("login"))


@notes_page.route("/edit_note", methods=["POST", "GET"])
def edit_note():
    if "user" in session:
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
    else:
        return redirect(url_for("login"))


@notes_page.route("/search_note", methods=["POST", "GET"])
def search_note():
    if "user" in session:
        username = session["user"]
        select_notes = NotesController.select_notes()
        select_categories = CategoriesController.select_categories()
        if request.method == "POST":
            try:
                search_value = request.form["search_value"]

                result = notes_controller.search_note(
                    search_value=search_value)
                print(search_value)
            except Error as error:
                print(error)

        return render_template("note/notes.html.j2", result=result, notes=select_notes, categories=select_categories, username=username)
    else:
        return redirect(url_for("login"))


@notes_page.route("/filter_notes", methods=["POST", "GET"])
def filter_note():
    if "user" in session:
        username = session["user"]
        select_notes = NotesController.select_notes()
        select_categories = CategoriesController.select_categories()
        if request.method == "POST":
            try:
                filter_value = request.form["filter_value"]

                result = notes_controller.filter_notes(
                    filter_value=filter_value)
                print(filter_value)
            except Error as error:
                print(error)
        return render_template("note/notes.html.j2", result=result, notes=select_notes, categories=select_categories, username=username)
    else:
        return redirect(url_for("login"))


@notes_page.route("/")
def notes():
    if "user" in session:
        username = session["user"]
        select_notes = NotesController.select_notes()
        select_categories = CategoriesController.select_categories()
        return render_template("note/notes.html.j2", notes=select_notes, categories=select_categories, username=username)
    else:
        return redirect(url_for("login"))


@notes_page.route("/update_question", methods=["POST"])
def update_question():
    if "user" in session:
        if request.method == "POST":
            try:
                note_id = request.form["note_id"]  # Retrieve note_id
                # Retrieve the generated question
                generated_question = request.form["note"]
                api_key = "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"
                test_gpt = TestGPT(api_key)
                open_question = test_gpt.generate_open_question(
                    generated_question)

                # Update the question in the database using the QuestionsController
                QuestionsController.update_question(
                    note_id=note_id, question=open_question)

                # Redirect to the note page or any desired page after successful update
                return redirect(url_for('notes.note', note_id=note_id))

            except Error as error:
                print(error)
                # Redirect to an error page or handle the error as needed

        # Redirect to the notes page if not a POST request or if user not in session
        return redirect(url_for('notes.notes'))
    else:
        return redirect(url_for("login"))

# @notes_page.route("/generate_question/<int:note_id>", methods=["POST"])
# def generate_question_server(note_id):
#     if "user" in session:
#         if request.method == "POST":
#             try:
#                 note = request.form["note"]
#                 generated_question = process_note_to_question(note)
#                 return json.dumps({"question": generated_question})
#             except Error as error:
#                 print(error)
#         return json.dumps({"error": "Unable to generate a question"})
#     else:
#         return json.dumps({"error": "User not authenticated"}), 401


# def process_note_to_question(note):
#     note_text = note[0][6]
#     api_key = "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"
#     test_gpt = TestGPT(api_key)
#     open_question = test_gpt.generate_open_question(note_text)

#     return open_question
