from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import TextAreaField,SubmitField,StringField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Update bio.',validators = [Required()])
    submit = SubmitField('Save Changes')

class PostAPitch (FlaskForm):
    title = StringField('Title of the pitch',validators = [Required()])
    content = TextAreaField('Pitch content.',validators = [Required()])
    submit = SubmitField('Pitch')