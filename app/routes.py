from app import app
from app import db
from app import socketio
from flask import render_template
from flask import redirect
from flask import flash
from flask import session
from flask import request
from datetime import datetime
from .forms import LoginForm
from .forms import ComposeForm
from .forms import RegisterForm
from .forms import SearchForm
from .forms import SortForm
from .models import Drafts
from .models import DeletedAccounts
from .models import User 
from .models import Message
from .models import ToDo
from .forms import ToDoForm
from flask_login import current_user
from flask_login import login_user 
from flask_login import logout_user
from flask_login import login_required
from sqlalchemy import collate
from flask import url_for
from werkzeug.security import generate_password_hash
from flask_socketio import SocketIO, send

# Main page for registering / login
@app.route("/")
def index():
    return render_template('index.html')

# Dashboard route that is only accessible when the user is logged in
@app.route("/dashboard/", methods=['GET', 'POST'])
@login_required
def dashboard():
    form = SortForm()
    # Fetch the user_id of the current user and the current user's messages
    user_id = User.query.filter_by(username=current_user.username).first().id
    # Fetch the user's messages
    messages = User.query.filter_by(username=current_user.username).first().messages 
    if form.validate_on_submit(): 
        if form.sortByOptions.data == 'alphabet':
            # Sort the messages by subject in alphabetical order
            messages = Message.query.filter_by(receiving_user=user_id).order_by(collate(Message.subject, 'NOCASE')).all()
        if form.sortByOptions.data == 'oldest':
            # Sort the messages by oldest to newest
            messages = Message.query.filter_by(receiving_user=user_id).order_by(Message.timestamp).all()
        if form.sortByOptions.data == 'newest':
            # Sort the messages by newest to oldest
            messages = Message.query.filter_by(receiving_user=user_id).order_by(Message.timestamp).all()
            messages.reverse()

    # Render the dashboard template with the current user object and their messages passed through
    # The User class is passed through in order to do queries on the User table.
    return render_template('dashboard.html', user=current_user, messages=messages, class1=User, form=form)

# Route for composing messages
@app.route("/compose/", methods=['GET', 'POST'])
@login_required
def compose():
    form = ComposeForm()
    if form.validate_on_submit(): 
        # Check if the submit button is being clicked
        if form.submit.data:
            if User.query.filter_by(username=form.receiving_username.data).first() is not None:
                # When the form is submitted, a message object containing the subject, body, sending user, and receiving user is created.
                # The timestamp is automatically generated at time of creation.
                dateAndTime = datetime.now()
                message = Message(subject=form.subject.data, body=form.body.data, sending_user=current_user.id, receiving_user=User.query.filter_by(username=form.receiving_username.data).first().id, timestamp=dateAndTime)
                # Add the message to the database and commit the changes
                db.session.add(message)
                db.session.commit()
                # Redirect the user to the dashboard afterwards
                return redirect(url_for('dashboard'))
            else:
                flash("User does not exist")
        else:
            if User.query.filter_by(username=form.receiving_username.data).first() is not None:
                # When the form is submitted, a message object containing the subject, body, sending user, and receiving user is created.
                # The timestamp is automatically generated at time of creation.
                dateAndTime = datetime.now()
                draft = Drafts(subject=form.subject.data, body=form.body.data, sending_user=current_user.id, receiving_user=User.query.filter_by(username=form.receiving_username.data).first().id, timestamp=dateAndTime)
                # Add the message to the database and commit the changes
                db.session.add(draft)
                db.session.commit()
                # Redirect the user to the dashboard afterwards
                return redirect(url_for('dashboard'))
            else:
                flash("User does not exist")
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
    # Add the username to the deleted username table.
    deletedUsername = DeletedAccounts(username=u.username)
    u.username = None
    u.password = None
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
            else: 
                flash("Incorrect credentials!")

    # Render the login page
    return render_template('login.html', form=form)

# Route for the register page
@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit(): 
        # If the form is submitted, check if the username is unique and does not exist in the database
        if form.validate_username(form.username) and DeletedAccounts.validateUsername(form.username.data) is True: 
            # If so, create a new user object containing the name, the username, the hashed password, and add it to the database.
            user = User(name=form.firstname.data + " " + form.lastname.data, username=form.username.data, password=generate_password_hash(form.password.data))
            # Add the user to the database and then commit the changes
            db.session.add(user)
            db.session.commit()
            # Redirect the user to the login page.
            return redirect(url_for('login'))
        else: 
            flash("Username already exists!")
    return render_template('register.html', form=form)

# To do list route
@app.route("/todo/", methods=["POST", "GET"])
@login_required
def todo():
    form = ToDoForm()
    if form.validate_on_submit():
        # Add the to do item to the databaes
        toDoItem = ToDo(description=form.task.data, user=current_user.id)
        db.session.add(toDoItem)
        db.session.commit()
        # Redirect to the todo page
        return redirect(url_for('todo'))
    # Render the todo page
    return render_template("todolist.html", form=form, list=current_user.todos)

# Delete the todo page
@app.route("/deleteTodo/<int:id>", methods=["POST", "GET"])
@login_required
def deleteToDo(id):
    # Query the id, set the boolean to true, then commit the changes
    toDoItem = ToDo.query.filter_by(id=id).first()
    toDoItem.done = True
    db.session.commit()
    return redirect(url_for('todo'))


# Search page
@app.route('/search', methods=["POST", "GET"])
@login_required
def search():
    form = SearchForm()
    searchTerm = form.searched.data
    filtered_messages = []
    if form.validate_on_submit():
        # Checks both the user's id and the message within the database to filter the user who composed the message and the receiver
        user_id = User.query.filter_by(username=current_user.username).first().id
        messages = Message.query.filter_by(receiving_user=user_id).all()
        for message in messages: 
            # Checks through messages to find matching different in the subject section and body section of the message.
            if message.body.find(searchTerm) != -1 or message.subject.find(searchTerm) != -1:
                filtered_messages.append(message)
   # Returns the email that fits the search parameters the user gives
    return render_template("search.html", form=form, filtered=filtered_messages, class1=User)

@socketio.on('message')
def handle_message(message):
    send(message, broadcast=True)

@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    return render_template('chat.html', username=current_user.username)

@app.route('/drafts/', methods=['GET', 'POST'])
@login_required
def draft():
    return render_template('drafts.html', drafts=Drafts.query.filter_by(sending_user=current_user.id, visible=True).all(), class1=User)

@app.route('/sendDraft/<int:id>', methods=['GET', 'POST'])
def sendDraft(id):
    if Drafts.query.filter_by(id=id).first().receiving_user == current_user.id:
        time = datetime.now()
        draft = Drafts.query.filter_by(id=id).first()
        draft.visible = False
        message = Message(subject=draft.subject, body=draft.body, sending_user=draft.sending_user, receiving_user=draft.receiving_user, timestamp=time)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('drafts'))

@app.route('/editprofile/<int:id>', methods=['GET', 'POST'])
@login_required
def editprofile(id):
    form = editProfile()
    updated =  User.query.get(id)
    request.method == "POST"
    updated.username == request.form['Username']
    updated.name = request.form['Name']
    updated.lastname = request.form['Last Name']
    updated.password = request.form['Password']
    



