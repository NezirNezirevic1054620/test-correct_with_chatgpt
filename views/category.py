from flask import Blueprint, request, render_template, redirect, url_for, session
from sqlite3 import Error

from controllers.categories_controller import CategoriesController
from views.forms.category_form import CategoryForm

category_page = Blueprint("category", __name__, url_prefix="/categories", template_folder="templates/category",
                          static_folder="static")
category_controller = CategoriesController()


@category_page.route("/create_category", methods=["GET", "POST"])
def create_category():
    if "user" in session:
        username = session["user"]
        category_form = CategoryForm()
        if category_form.validate_on_submit():
            omschrijving = category_form.omschrijving.data
            category_controller.insert_category(omschrijving=omschrijving)
            return redirect(url_for('category.categories'))
        else:
            print(category_form.errors)
        return render_template("category/create_category.html.j2", form=category_form, username=username)
    else:
        return redirect(url_for("login"))


@category_page.route("/")
def categories():
    if "user" in session:
        username = session["user"]
        select_categories = CategoriesController.select_categories()
        return render_template("category/categories.html.j2", categories=select_categories, username=username)
    else:
        return redirect(url_for("login"))


@category_page.route("/delete_category", methods=["POST", "GET"])
def delete_category():
    if "user" in session:
        if request.method == "POST":
            try:
                category_id = request.form["category_id"]

                category_controller.delete_category(category_id=category_id)
            except Error as error:
                print(error)
        return redirect(url_for('category.categories'))
    else:
        return redirect(url_for("login"))


@category_page.route("/category/<int:category_id>", methods=["POST", "GET"])
def category(category_id):
    if "user" in session:
        username = session["user"]
        select_category = None
        if request.method == "POST":
            try:
                category_id = request.form["category_id"]
                select_category = category_controller.select_category(category_id=category_id)
                print(category)
            except Error as error:
                print(error)
        return render_template("category/category.html.j2", category=select_category, category_id=category_id,
                               username=username)
    else:
        return redirect(url_for("login"))


@category_page.route("/update_category", methods=["POST", "GET"])
def update_category():
    if "user" in session:
        username = session["user"]
        if request.method == "POST":
            try:
                category_id = request.form["category_id"]
                omschrijving = request.form["omschrijving"]

                category_controller.update_category(category_id=category_id, omschrijving=omschrijving)
                return redirect(url_for('category.categories'))
            except Error as error:
                print(error)
        return render_template("category/category.html.j2", username=username)
    else:
        return redirect(url_for("login"))


@category_page.route("/search_category", methods=["POST", "GET"])
def search_category():
    if "user" in session:
        username = session["user"]
        select_categories = CategoriesController.select_categories()
        if request.method == "POST":
            try:
                search_value = request.form["search_value"]

                result = category_controller.search_category(search_value=search_value)
                print(search_value)
            except Error as error:
                print(error)

        return render_template("category/categories.html.j2", result=result, categories=select_categories,
                               username=username)
    else:
        return redirect(url_for("login"))
