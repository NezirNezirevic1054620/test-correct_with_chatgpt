from models.category_model import CategoryModel

DATABASE_FILE = "/Users/nezirnezirevic/Desktop/wp2-2023-mvc-1e5-nlbl/databases/testgpt.db"


def test_selected_note():
    category = None
    mydict = {}
    category_model = CategoryModel(DATABASE_FILE)
    selected_category = category_model.select_category(category_id=1)
    for category in selected_category:
        mydict = {
            'category_id': category[0],
            'omschrijving': category[1],
            'date_created': category[2],

        }
    print(mydict)
    assert dict(category) == mydict
