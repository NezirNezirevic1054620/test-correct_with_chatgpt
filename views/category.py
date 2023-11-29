from flask import Blueprint, request, render_template, redirect, url_for
from sqlite3 import Error

from controllers.categories_controller import CategoriesController
from views.forms.category_form import CategoryForm

category_page = Blueprint("category", __name__, url_prefix="/category", template_folder="templates", static_folder="static")
category_controller = CategoriesController()


@category_page.route("/create_category", methods=["GET", "POST"])
def create_category():
    category_form = CategoryForm()
    if category_form.validate_on_submit():
        omschrijving = category_form.omschrijving.data
        category_controller.insert_category(omschrijving=omschrijving)
        return redirect(url_for('category.categories'))
    else:
        print(category_form.errors)
    return render_template("create_category.html.j2", form=category_form)


@category_page.route("/categories")
def categories():
    select_categories = CategoriesController.select_categories()
    return render_template("categories.html.j2", categories=select_categories)


@category_page.route("/delete_category", methods=["POST", "GET"])
def delete_category():
    if request.method == "POST":
        try:
            category_id = request.form["category_id"]

            category_controller.delete_category(category_id=category_id)
        except Error as error:
            print(error)
    return redirect(url_for('category.categories'))


@category_page.route("/select_category", methods=["POST", "GET"])
def select_category():
    if request.method == "POST":
        try:
            category_id = request.form["category_id"]
            category = category_controller.select_category(category_id=category_id)
            print(category)
        except Error as error:
            print(error)
    return render_template("category.html.j2", category=category)


@category_page.route("/update_category", methods=["POST", "GET"])
def update_category():
    if request.method == "POST":
        try:
            category_id = request.form["category_id"]
            omschrijving = request.form["omschrijving"]

            category_controller.update_category(category_id=category_id, omschrijving=omschrijving)
            return redirect(url_for('category.categories'))
        except Error as error:
            print(error)
    return render_template("category.html.j2")
