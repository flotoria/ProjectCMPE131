
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from .models import User 

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    # This method simply validates whether the username in the parameter matches a username in the database
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first() is None:
            raise ValidationError("Username does not exist.")
        return True
    
class RegisterForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators = [DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    
    # This method simply validates whether the username is unique, return True, if not, return False
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first() is None:
            return True
        return False
    
        
class ComposeForm(FlaskForm):
    receiving_username = StringField('Receiving User', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    body = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

class SearchForm(FlaskForm):
	searched = StringField("Search", validators=[DataRequired()])
	submit = SubmitField("Submit")

class ToDoForm(FlaskForm):
    task = StringField('Enter task', validators=[DataRequired()])
    submit = SubmitField('Add')
    close = SubmitField('X')

    