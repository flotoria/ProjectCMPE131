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
from .forms import ToDoForm
from flask_login import current_user
from flask_login import login_user 
from flask_login import logout_user
from flask_login import login_required
from flask import url_for
from werkzeug.security import generate_password_hash


@app.route("/")
def index():
    return "Hello World!"

# Dashboard route that is only accessible when the user is logged in
@app.route("/dashboard/")
@login_required
def dashboard():
    # Fetch the user_id of the current user and the current user's messages
    user_id = User.query.filter_by(username=current_user.username).first().id
    messages = Message.query.filter_by(receiving_user=user_id).all()
    # Render the dashboard template with the current user object and their messages passed through
    # The User class is passed through in order to do queries on the User table.
    return render_template('dashboard.html', user=current_user, messages=messages, class1=User)

# Route for composing messages
@app.route("/compose/", methods=['GET', 'POST'])
@login_required
def compose():
    form = ComposeForm()
    if form.validate_on_submit(): 
        # When the form is submitted, a message object containing the subject, body, sending user, and receiving user is created.
        # The timestamp is automatically generated at time of creation.
        message = Message(subject=form.subject.data, body=form.body.data, sending_user=current_user.id, receiving_user=User.query.filter_by(username=form.receiving_username.data).first().id)
        # Add the message to the database and commit the changes
        db.session.add(message)
        db.session.commit()
        # Redirect the user to the dashboard afterwards
        return redirect(url_for('dashboard'))
    # Return the render template of the compose page
    return render_template('compose.html', user=current_user, form=form)

# Route to logout the user
@app.route("/logout/")
@login_required
def logout():
    # Logout the user
    logout_user()
    # Redirect the user back to the login page
    return redirect(url_for('login'))

# Route for deleting account
@app.route("/delete/", methods=['GET', 'POST'])
@login_required
def delete():
    # Fetch the user in the database
    u = User.query.filter_by(id=current_user.id).first()
    # Delete the user from the database then commit those changes
    db.session.delete(u)
    db.session.commit()
    # Redirect the user back to the login page
    return render_template('delete.html')

# Route for the login page
@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check if the username exists within the database
        if form.validate_username(form.username) == True: 
            # If the username exists, check whether the password inputted matches the password (hashed) in the database.
            if(User.query.filter_by(username=form.username.data).first().check_password(form.password.data) == True): 
                # If so, login and redirect the user to the dashboard
                login_user(User.query.filter_by(username=form.username.data).first())
                return redirect(url_for('dashboard'))
    # Render the login page
    return render_template('login.html', form=form)

# Route for the register page
@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit(): 
        # If the form is submitted, check if the username is unique and does not exist in the database
        if form.validate_username(form.username) == True: 
            # If so, create a new user object containing the name, the username, the hashed password, and add it to the database.
            user = User(name=form.firstname.data + " " + form.lastname.data, username=form.username.data, password=generate_password_hash(form.password.data))
            # Add the user to the database and then commit the changes
            db.session.add(user)
            db.session.commit()
            # Redirect the user to the login page.
            return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/todo/")
@login_required
def todo():
    form = ToDoForm()
    if form.validate_on_submit():
        if form.task == True:
            
            return 0
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