""" Tests for the CategoryModel """
from models.category_model import CategoryModel

DATABASE_FILE = "databases/testgpt.db"


def test_get_all_categories():
    """Method checks if the output is a dictionary"""
    category = None
    mydict = {}
    category_model = CategoryModel(DATABASE_FILE)
    categories = category_model.get_all_categories()
    for category in categories:
        mydict = {
            "category_id": category[0],
            "omschrijving": category[1],
            "date_created": category[2],
        }
    assert dict(category) == mydict


def test_insert_category():
    """Test if the category gets inserted into the database"""
    pass


def test_update_category():
    """Test if the category gets updated in the database"""
    pass


def test_delete_category():
    """Test if the category gets deleted from the database"""
    pass


def test_search_category():
    category_model = CategoryModel(DATABASE_FILE)
    searched_category = category_model.search_categories(search_value="Onboarding")
    if searched_category is not None:
        for category in searched_category:
            print(dict(category))
    else:
        print("No note")
