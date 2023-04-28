
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from .models import User 

# Flask form for the login page
class LoginForm(FlaskForm):
    # Input fields for the username and password
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    
    # This method simply validates whether the username in the parameter matches a username in the database
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first() is None:
            raise ValidationError("Username does not exist.")
        return True
    
# Flask form  for registering a user
class RegisterForm(FlaskForm):
    # Input fields for the first name, last name, username, password.
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators = [DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # Submit button
    submit = SubmitField('Register')
    
    # This method simply validates whether the username is unique, return True, if not, return False
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first() is None:
            return True
        return False
    

# Flask form for composing a message        
class ComposeForm(FlaskForm):
    # Fields for the receiving user, subject, and body message.
    receiving_username = StringField('Receiving User', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    body = StringField('Message', validators=[DataRequired()])
    # Submit button
    submit = SubmitField('Send')

# Flask form for submitting a search query
class SearchForm(FlaskForm):
	searched = StringField("Search", validators=[DataRequired()])
    # Submit button
	submit = SubmitField("Submit")

# To-do list form
class ToDoForm(FlaskForm):
    # Input for entering the task
    task = StringField('Enter task', validators=[DataRequired()])
    # Submit button
    submit = SubmitField('Add')

# Form to help the user sort their messages
class SortForm(FlaskForm):
    sortByOptions = SelectField("Sort Options:", choices=[('alphabet', 'Sort by Alphabetical Order'), ('oldest', 'Sort by Oldest'), ('newest', 'Sort by Newest')])
    # Submit button
    submit = SubmitField('Sort')