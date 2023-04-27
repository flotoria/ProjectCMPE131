from app import app
from app import db
from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm
from .forms import ComposeForm
from .forms import RegisterForm
from .forms import SearchForm
from .models import User 
from .models import Message
from flask_login import current_user
from flask_login import login_user 
from flask_login import logout_user
from flask_login import login_required
from flask import url_for
from werkzeug.security import generate_password_hash


@app.route("/")
def index():
    return "Hello World!"

# Dashboard route, only accessible if user is logged in
@app.route("/dashboard/")
@login_required
def dashboard():
    user_id = User.query.filter_by(username=current_user.username).first().id
    messages = Message.query.filter_by(receiving_user=user_id).all()
    return render_template('dashboard.html', user=current_user, messages=messages, class1=User)

@app.route("/compose/", methods=['GET', 'POST'])
@login_required
def compose():
    form = ComposeForm()
    if form.validate_on_submit(): 
        message = Message(subject=form.subject.data, body=form.body.data, sending_user=current_user.id, receiving_user=User.query.filter_by(username=form.receiving_username.data).first().id)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('compose.html', user=current_user, form=form)

# Logs out the user
@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/delete/", methods=['GET', 'POST'])
@login_required
def delete():
    u = User.query.filter_by(id=current_user.id).first()
    db.session.delete(u)
    db.session.commit()
    flash('Account deleted.')
    print('Account deleted.')
    return render_template('delete.html')
# Route for the login page, simply checks whether the username and password are valid, then redirect to a certain page.
@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.validate_username(form.username) == True: 
            if(User.query.filter_by(username=form.username.data).first().check_password(form.password.data) == True): 
                login_user(User.query.filter_by(username=form.username.data).first())
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

# Route for the register page
@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit(): 
        if form.validate_username(form.username) == True: 
            user = User(name=form.firstname.data + " " + form.lastname.data, username=form.username.data, password=generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/todo/")
# @login_required
def todo():
    return render_template("todo.html")

# Search page
@app.route('/search', methods=["POST", "GET"])
@login_required
def search():
    form = SearchForm()
    searchTerm = form.searched.data
    filtered_messages = []
    if form.validate_on_submit():
        user_id = User.query.filter_by(username=current_user.username).first().id
        messages = Message.query.filter_by(receiving_user=user_id).all()
        for message in messages: 
            if message.body.find(searchTerm) != -1 or message.subject.find(searchTerm) != -1:
                filtered_messages.append(message)
   
    return render_template("search.html", form=form, filtered=filtered_messages, class1=User)