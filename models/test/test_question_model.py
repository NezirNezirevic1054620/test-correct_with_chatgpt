"""Tests for the QuestionModel"""
from models.question_model import QuestionModel

DATABASE_FILE = (
    "databases/testgpt.db"
)


def test_get_all_questions():
    """Method checks if the output is a dictionary"""
    question = None
    mydict = {}
    question_model = QuestionModel(DATABASE_FILE)
    questions = question_model.get_all_questions()
    for question in questions:
        mydict = {
            "questions_id": question[0],
            "note_id": question[1],
            "exam_question": question[2],
            "date_created": question[3],
            "title": question[5],
            "note_source": question[6],
            "is_public": question[7],
            "teacher_id": question[8],
            "category_id": question[9],
            "note": question[10],
        }
    assert dict(question) == mydict


def test_insert_question():
    """Test if the question gets inserted into the database"""
    pass


def test_update_question():
    """Test if the question gets updated in the database"""
    pass


def test_delete_question():
    """Test if the question gets deleted from the database"""
    pass
