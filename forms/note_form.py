from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import Optional, DataRequired, Length


class NoteForm(FlaskForm):
    title = StringField("title", validators=[Optional()])
    note_source = StringField(
        "note_source", validators=[DataRequired(), Length(min=10, max=40)]
    )
    is_public = IntegerField("is_public")
    teacher_id = IntegerField("teacher_id", validators=[DataRequired()])
    category_id = IntegerField("category_id", validators=[DataRequired()])
    note = TextAreaField("note", validators=[DataRequired(), Length(min=10, max=500)])
