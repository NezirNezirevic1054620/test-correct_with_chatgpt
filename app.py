from flask import Flask, render_template
from controllers.notes_controller import NotesController
from controllers.categories_controller import CategoriesController
from flask import request
from sqlite3 import Error

app = Flask(__name__, template_folder="templates", static_folder="static")

notes_controller = NotesController()


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html.j2")


@app.route("/create_note", methods=["POST", "GET"])
def create_note():
    select_categories = CategoriesController.select_categories()
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
        except Error as error:
            print(error)
    return render_template("create_note.html.j2", categories=select_categories)


@app.route("/notes")
def notes():
    select_notes = NotesController.select_notes()
    return render_template("notes.html.j2", notes=select_notes)


if __name__ == "__main__":
    app.run(debug=True)
