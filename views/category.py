from flask import Blueprint, request, render_template
from sqlite3 import Error

from controllers.categories_controller import CategoriesController

category_page = Blueprint("category", __name__, url_prefix="/category", template_folder="templates", static_folder="static")
category_controller = CategoriesController()


@category_page.route("/create_category", methods=["GET", "POST"])
def create_category():
    if request.method == "POST":
        try:
            omschrijving = request.form["omschrijving"]

            category_controller.insert_category(omschrijving=omschrijving)

        except Error as error:
            print(error)
    return render_template("create_category.html.j2")


@category_page.route("/categories")
def categories():
    select_categories = CategoriesController.select_categories()
    return render_template("categories.html.j2", categories=select_categories)

