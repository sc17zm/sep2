from flask_wtf import Form
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import TextField,validators,SubmitField

from wtforms.validators import DataRequired

class loginform(Form):
    username = StringField('Username', [validators.required(), validators.length(max=25)])
    password = StringField('Password', [validators.required(), validators.length(max=25)])

#create the form
class AddIssueForm(Form):
     issue = TextField('Issue', validators=[DataRequired()])
     solution = TextAreaField('Solution', validators=[DataRequired()])

class SearchForm(Form):
    search=StringField('')

#create the form
class AddDoctorForm(Form):
     name = TextField('Name:', validators=[DataRequired()])
     surname = TextField('Surname:', validators=[DataRequired()])
     telephone=TextField('Phone number:', validators=[DataRequired()])