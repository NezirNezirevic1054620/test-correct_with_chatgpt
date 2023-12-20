from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import Optional, DataRequired, Length


class NoteForm(FlaskForm):
    title = StringField("title", validators=[Optional()])
    note_source = StringField(
        "note_source", validators=[DataRequired(), Length(min=4, max=100)]
    )
    is_public = IntegerField("is_public")
    teacher_id = IntegerField("teacher_id", validators=[DataRequired()])
    category_id = IntegerField("category_id", validators=[DataRequired()])
    note = StringField("note", validators=[DataRequired(), Length(min=10, max=1500)])
