from models.note_model import NoteModel

DATABASE_FILE = "/Users/nezirnezirevic/Desktop/wp2-2023-mvc-1e5-nlbl/databases/testgpt.db"


def test_get_all_notes():
    note = None
    mydict = {}
    note_model = NoteModel(DATABASE_FILE)
    notes = note_model.get_all_notes(teacher_id=str(5))
    for note in notes:
        mydict = {
            "note_id": note[0],
            'title': note[1],
            'note_source': note[2],
            'is_public': note[3],
            'teacher_id': note[4],
            'category_id': note[5],
            'note': note[6],
            'date_created': note[7],
            'omschrijving': note[9]
        }
    assert dict(note) == mydict


def test_search_note():
    note_model = NoteModel(DATABASE_FILE)
    seached_note = note_model.search_note(teacher_id=5, search_value="python")
    if seached_note is not None:
        for note in seached_note:
            print(dict(note))
    else:
        print("No note")


if __name__ == "__main__":
    test_search_note()
    test_get_all_notes()
