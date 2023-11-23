from flask import Flask, render_template

from views.note import notes_page

app = Flask(__name__, template_folder="templates", static_folder="static")
app.register_blueprint(notes_page)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html.j2")


if __name__ == "__main__":
    app.run(debug=True)
