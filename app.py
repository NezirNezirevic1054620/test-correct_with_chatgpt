from flask import Flask, render_template, request, session, redirect, url_for

from views.category import category_page
from views.note import notes_page

from controllers.teacher_controller import TeacherController
SECRET_KEY = "babababa"

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(notes_page)
app.register_blueprint(category_page)

teacher_controller = TeacherController()


@app.route("/",  methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def home():
    session.pop("user", None)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        result = teacher_controller.login(username=username, password=password)
        if result:
            session["user"] = username
            print(session["user"])
            return redirect(url_for("notes.notes"))
        else:
            return redirect(url_for("home"))

    return render_template("login.html.j2")


app.config['SECRET_KEY'] = SECRET_KEY


if __name__ == "__main__":
    app.run(debug=True)
