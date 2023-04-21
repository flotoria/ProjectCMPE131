from app import app
from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm
from .models import User 
from flask_login import current_user
from flask_login import login_user 
from flask_login import logout_user
from flask_login import login_required
from flask import url_for


@app.route("/")
def index():
    return "Hello World!"

# Route for the login page, simply checks whether the username and password are valid, then redirect to a certain page.
@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.validate_username(form.username) == True: 
            if(User.query.filter_by(username=form.username.data).first().check_password(form.password.data) == True): 
                return redirect(url_for('index'))
    return render_template('login.html', form=form)