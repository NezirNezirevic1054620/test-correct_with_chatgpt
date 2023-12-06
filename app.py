from flask import Flask, render_template, request, session, redirect, url_for

from views.category import category_page
from views.note import notes_page

from controllers.teacher_controller import TeacherController
from views.teacher import teachers_page

SECRET_KEY = "babababa"

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(notes_page)
app.register_blueprint(category_page)
app.register_blueprint(teachers_page)

teacher_controller = TeacherController()


@app.route("/",  methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    session.pop("user", None)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        result = teacher_controller.login(username=username, password=password)
        if result:
            session["user"] = username
            session["is_admin"] = result[0][5]
            print(session["is_admin"])
            print(session["user"])
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("login"))

    return render_template("login.html.j2")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user" in session:
        username = session["user"]
        return render_template("index.html.j2", username=username)
    else:
        return redirect(url_for("login"))


@app.route("/admin_dashboard", methods=["GET", "POST"])
def admin_dashboard():
    if "user" in session:
        username = session["user"]
        return render_template("beheer.html.j2", username=username)
    else:
        return redirect(url_for("login"))


app.config['SECRET_KEY'] = SECRET_KEY


if __name__ == "__main__":
    app.run(debug=True)
