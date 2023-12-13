""" Testing NoteModel """
from models.note_model import NoteModel

DATABASE_FILE = (
    "/Users/nezirnezirevic/Desktop/wp2-2023-mvc-1e5-nlbl/databases/testgpt.db"
)


def test_get_all_notes():
    """Method checks if the output is a dictionary"""
    note = None
    mydict = {}
    note_model = NoteModel(DATABASE_FILE)
    teacher_id = 5
    notes = note_model.get_all_notes(teacher_id=str(teacher_id))
    for note in notes:
        mydict = {
            "note_id": note[0],
            "title": note[1],
            "note_source": note[2],
            "is_public": note[3],
            "teacher_id": note[4],
            "category_id": note[5],
            "note": note[6],
            "date_created": note[7],
            "omschrijving": note[9],
        }
    assert dict(note) == mydict
