"""Note controller with all its routes"""
from sqlite3 import Error
import os

from flask import Blueprint, request, render_template, redirect, url_for, session

from models.category_model import CategoryModel
from models.note_model import NoteModel
from models.teacher_model import TeacherModel
from models.question_model import QuestionModel
from forms.note_form import NoteForm
from lib.testgpt.testgpt import TestGPT

notes_page = Blueprint(
    "notes",
    __name__,
    url_prefix="/notes",
    template_folder="templates/note",
    static_folder="static",
)

DATABASE_FILE = "databases/testgpt.db"


@notes_page.route("/create_note", methods=["POST", "GET"])
def create_note():
    """Create note route that creates a new note and inserts it into the database"""
    if "user" in session:
        note_model = NoteModel(DATABASE_FILE)
        teacher_model = TeacherModel(DATABASE_FILE)
        category_model = CategoryModel(DATABASE_FILE)
        username = session["user"]
        note_form = NoteForm()
        select_categories = category_model.get_all_categories()
        select_teachers = teacher_model.get_all_teachers()
        if note_form.validate_on_submit():
            title = note_form.title.data
            note_source = note_form.note_source.data
            is_public = note_form.is_public.data
            teacher_id = note_form.teacher_id.data
            category_id = note_form.category_id.data
            note_text = note_form.note.data

            note_model.insert_note(
                title=title,
                note_source=note_source,
                is_public=is_public,
                teacher_id=teacher_id,
                category_id=category_id,
                note=note_text,
            )
            return redirect(url_for("notes.notes"))
        return render_template(
            "note/create_note.html.j2",
            categories=select_categories,
            teachers=select_teachers,
            form=note_form,
            username=username,
        )

    return redirect(url_for("login"))


@notes_page.route("/delete_note", methods=["GET", "POST"])
def delete_note():
    """Delete note route that deletes a specific note from the database"""
    if "user" in session:
        note_model = NoteModel(DATABASE_FILE)
        if request.method == "POST":
            try:
                note_id = request.form["note_id"]
                note_model.delete_note(note_id=note_id)

            except Error as error:
                print(error)

        return redirect(url_for("notes.notes"))

    return redirect(url_for("login"))


@notes_page.route("/note/<int:note_id>", methods=["POST", "GET"])
def note(note_id):
    """Note route that displays a sepcific note from the database"""
    if "user" in session:
        note_model = NoteModel(DATABASE_FILE)
        teacher_model = TeacherModel(DATABASE_FILE)
        category_model = CategoryModel(DATABASE_FILE)
        question_model = QuestionModel(DATABASE_FILE)
        username = session["user"]
        select_note = None
        select_question = None
        select_categories = category_model.get_all_categories()
        select_teachers = teacher_model.get_all_teachers()
        if request.method == "POST":
            try:
                note_id = request.form["note_id"]
                select_note = note_model.select_note(note_id=note_id)
                select_question = question_model.select_question_by_note(
                    note_id=note_id
                )
            except Error as error:
                print(error)
        return render_template(
            "note/note.html.j2",
            note=select_note,
            teachers=select_teachers,
            categories=select_categories,
            questions=select_question,
            note_id=note_id,
            username=username,
        )

    return redirect(url_for("login"))


@notes_page.route("/edit_note", methods=["POST", "GET"])
def edit_note():
    """Edit note route that updates the changed fields from the note into the database"""
    if "user" in session:
        note_model = NoteModel(DATABASE_FILE)
        if request.method == "POST":
            try:
                title = request.form["title"]
                note_source = request.form["note_source"]
                is_public = request.form["is_public"]
                teacher_id = request.form["teacher_id"]
                category_id = request.form["category_id"]
                note_id = request.form["note_id"]
                note_text = request.form["note"]
                print(teacher_id)
                note_model.update_note(
                    title=title,
                    note_source=note_source,
                    is_public=is_public,
                    teacher_id=teacher_id,
                    category_id=category_id,
                    note=note_text,
                    note_id=note_id,
                )
            except Error as error:
                print(error)

        return redirect(url_for("notes.notes"))

    return redirect(url_for("login"))


@notes_page.route("/search_note", methods=["POST", "GET"])
def search_note():
    if "user" in session:
        result = None
        note_model = NoteModel(DATABASE_FILE)
        category_model = CategoryModel(DATABASE_FILE)
        username = session["user"]
        teacher_id = session["teacher_id"]
        select_notes = note_model.get_all_notes(teacher_id=str(teacher_id))
        select_categories = category_model.get_all_categories()

        if request.method == "POST":
            try:
                search_value = request.form["search_value"]
                page = request.args.get("page", default=1, type=int)
                entries_per_page = 20
                offset = (page - 1) * entries_per_page

                result = note_model.search_note(
                    teacher_id=str(teacher_id),
                    search_value=str(search_value),
                    offset=offset,
                    limit=entries_per_page,
                )

                total_entries = len(result) if result else len(select_notes)

                return render_template(
                    "note/notes.html.j2",
                    result=result,
                    notes=select_notes,
                    categories=select_categories,
                    username=username,
                    page=page,
                    entries_per_page=entries_per_page,
                    total_entries=total_entries,
                )

            except Error as error:
                print(error)

        return render_template(
            "note/notes.html.j2",
            result=result,
            notes=select_notes,
            categories=select_categories,
            username=username,
            page=1,
            entries_per_page=20,
            total_entries=len(result) if result else len(select_notes),
        )

    return redirect(url_for("login"))


@notes_page.route("/filter_note_by_category", methods=["POST", "GET"])
def filter_note_by_category():
    """Filter note route that filters the notes based on category that they belong to"""
    if "user" in session:
        result = None
        note_model = NoteModel(DATABASE_FILE)
        category_model = CategoryModel(DATABASE_FILE)
        username = session["user"]
        teacher_id = session["teacher_id"]
        select_notes = note_model.get_all_notes(teacher_id=str(teacher_id))
        select_categories = category_model.get_all_categories()
        if request.method == "POST":
            try:
                filter_value = request.form["filter_value"]
                page = request.args.get("page", default=1, type=int)
                entries_per_page = 20
                offset = (page - 1) * entries_per_page

                result = note_model.filter_note_by_category(
                    teacher_id=str(teacher_id),
                    filter_value=filter_value,
                    offset=offset,
                    limit=entries_per_page,
                )

                total_entries = len(result) if result else len(select_notes)

                return render_template(
                    "note/notes.html.j2",
                    result=result,
                    notes=select_notes,
                    categories=select_categories,
                    username=username,
                    page=page,
                    entries_per_page=entries_per_page,
                    total_entries=total_entries,
                )

            except Error as error:
                print(error)

        return render_template(
            "note/notes.html.j2",
            result=result,
            notes=select_notes,
            categories=select_categories,
            username=username,
            page=1,
            entries_per_page=20,
            total_entries=len(result) if result else len(select_notes),
        )

    return redirect(url_for("login"))


@notes_page.route("/filter_note_by_teacher", methods=["POST", "GET"])
def filter_note_by_teacher():
    if "user" in session:
        result = None
        note_model = NoteModel(DATABASE_FILE)
        username = session["user"]
        teacher_id = session["teacher_id"]
        select_notes = note_model.get_all_notes(teacher_id=str(teacher_id))

        if request.method == "POST":
            try:
                page = request.args.get("page", default=1, type=int)
                entries_per_page = 20
                offset = (page - 1) * entries_per_page

                result = note_model.filter_note_by_teacher(
                    offset=offset, limit=entries_per_page
                )

                total_entries = len(result) if result else len(select_notes)

                return render_template(
                    "note/notes.html.j2",
                    result=result,
                    notes=select_notes,
                    username=username,
                    page=page,
                    entries_per_page=entries_per_page,
                    total_entries=total_entries,
                )

            except Error as error:
                print(error)

        return render_template(
            "note/notes.html.j2",
            result=result,
            notes=select_notes,
            username=username,
            page=1,
            entries_per_page=20,
            total_entries=len(result) if result else len(select_notes),
        )

    return redirect(url_for("login"))


@notes_page.route("/")
def notes():
    """Note route which displays paginated notes made by the user"""
    if "user" in session:
        note_model = NoteModel(DATABASE_FILE)
        category_model = CategoryModel(DATABASE_FILE)
        username = session["user"]
        teacher_id = session["teacher_id"]

        # Get the page number from the query parameters, default to 1 if not present
        page = request.args.get("page", default=1, type=int)

        # Set the number of entries per page
        entries_per_page = 20

        # Calculate the offset based on the page number
        offset = (page - 1) * entries_per_page

        # Get paginated notes
        select_notes = note_model.get_paginated_notes(
            teacher_id=str(teacher_id), offset=offset, limit=entries_per_page
        )
        total_entries = note_model.get_total_entries(teacher_id=str(teacher_id))

        select_categories = category_model.get_all_categories()
        return render_template(
            "note/notes.html.j2",
            notes=select_notes,
            categories=select_categories,
            username=username,
            page=page,
            entries_per_page=entries_per_page,
            total_entries=total_entries,
        )

    return redirect(url_for("login"))


@notes_page.route("/generate_question", methods=["POST"])
def generate_question():
    """Generate question route which connects to the OpenAI API and takes the note as paramater
    and generates a question and then inserts it into the database"""
    if "user" in session:
        question_model = QuestionModel(DATABASE_FILE)
        if request.method == "POST":
            try:
                selected_note = request.form["note"]
                note_id = request.form["note_id"]
                api_key = os.getenv("API_KEY")
                test_gpt = TestGPT(api_key)
                open_question = test_gpt.generate_open_question(selected_note)
                print(open_question)
                question_model.insert_question(
                    note_id=note_id, exam_question=open_question
                )
                return redirect(url_for("questions.questions"))
            except Error as error:
                print(error)

        return render_template("note/note.html.j2")

    return redirect(url_for("login"))
