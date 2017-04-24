from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import  Required, Length


class NameFrom(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileFrom(FlaskForm):
    name = StringField('Real name', validators=[Length(0,64)])
    location = StringField('Location', validators=[Length(0,64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

