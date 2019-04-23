from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import TextAreaField,SubmitField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Update bio.',validators = [Required()])
    submit = SubmitField('Submit')