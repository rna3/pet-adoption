from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """form for adding pets to the db"""

    name = StringField("Pet Name", validators = [InputRequired()])
    species = SelectField("Species",choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators = [Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Comments", validators=[Optional()])

class EditPetForm(FlaskForm):
    """form to edit the pet details"""

    photo_url = StringField("Photo URL", validators = [Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional()])
    available = BooleanField("Available?")    

