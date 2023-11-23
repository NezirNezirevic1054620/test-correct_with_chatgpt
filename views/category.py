from flask import Blueprint, request, render_template

from controllers.categories_controller import CategoriesController

category_page = Blueprint("category", __name__, url_prefix="/category", template_folder="templates", static_folder="static")


@category_page.route("/categories")
def categories():
    select_categories = CategoriesController.select_categories()
    return render_template("categories.html.j2", categories=select_categories)
