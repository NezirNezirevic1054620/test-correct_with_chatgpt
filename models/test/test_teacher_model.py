"""Tests for the TeacherModel"""
from models.teacher_model import TeacherModel

DATABASE_FILE = "databases/testgpt.db"


def test_get_all_teachers():
    """Method checks if the output is a dictionary"""
    teacher = None
    mydict = {}
    teacher_model = TeacherModel(DATABASE_FILE)
    teachers = teacher_model.get_all_teachers()
    for teacher in teachers:
        mydict = {
            "teacher_id": teacher[0],
            "display_name": teacher[1],
            "username": teacher[2],
            "teacher_password": teacher[3],
            "date_created": teacher[4],
            "is_admin": teacher[5],
        }
    assert dict(teacher) == mydict


def test_insert_teacher():
    """Test if the teacher gets inserted into the database"""
    pass


def test_update_teacher():
    """Test if the teacher gets updated in the database"""
    pass


def test_delete_teacher():
    """Test if the teacher gets deleted from the database"""
    pass
