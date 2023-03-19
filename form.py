from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Optional, URL


class EditProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    dob = DateField('Date of Birth', validators=[Optional()])
    phone_number = StringField('Phone Number', validators=[Optional(), Length(max=20)])
    bio = TextAreaField('Bio', validators=[Optional(), Length(max=1000)])
    image_url = StringField('Image URL', validators=[Optional(), URL(), Length(max=255)])
    submit = SubmitField('Save Changes')
