
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
    
        