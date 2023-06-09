# Cheese Mail
Cheese Mail is a web application where users can registered users can send messages, create tasks to do, compose and send emails to other users. 

## Installation
Clone the Cheese Mail Github Library
```
git clone https://github.com/flotoria/ProjectCMPE131.git
```

Use the packet manager pip to install libraries
```
pip install flask
pip install flask_sqlalchemy
pip install sqlalchemy
pip install flask_login
pip install werkzeug
pip install flask_wtf
pip install datetime
pip install wtforms
pip install flask_socketio
```

Initialize the database before running the program
``` 
python
from app import db
from app import app
app.app_context().push()
db.create_all()
exit()
``` 

It is important to note that if you do not have a folder called "image_database" inside app/static, there will be issues with uploading images. However, the folder
has been already included at your convenience. In the case that the folder isn't in there, make sure to create the folder.

## How to run
```
cd ProjectCMPE131
python run.py
```

## Usage
Access the web application with the url below
```
http://127.0.0.1:5000
```
## Technologies
Project is created with:
- Python version: 3
- HTML, CSS
- flask: login, sqlalchemy, wtf, socketio
- The Werkzeug python library
- datetimes library
- wtforms library

## How to use
Start by registering for a new account which will be stored in the database. Then you will be prompted into signing in with the information you have provided. Once that is completed you will reach the dashboard where there are 12 different buttons.


From there depending on which button you press, you will be taken to different parts of the website which will prompt users to enter the following information to do the specific requirement. The twelve buttons consist of Logout, Compose, Delete Account, Search, Sort, To-Do, Public Chat, Drafts, Edit Profile, Categories, Recycle Bin, and Sent Messages which corresponds to the different functional requirements implemented in the application.

## List of Features
- Logout - Selecting this button will log you out of the current account that you are using.
- Registration - Register for a new account with a name, username, and password.
- Compose - Selecting this button will bring you into the page for composing a message and from there you would have to input a receiving user, subject of the message, and body to be able to send a message to another user
- Delete Account - Pressing the delete account button will delete the user account that you are currently using and get rid of the information inside the database. 
- Search - Pressing the search button will allow you to search through the messages that have been sent to you that can be filtered by matching words inside the body and subject. 
- To-Do - Selecting the To-Do button will allow the user to create a to-do list of tasks that want to accomplish and when they are finished, they can mark it as done.
- Sort - Selecting the Sort button will allow user to interact with a drop-down bar that can sort the messages in the user's inbox by time and by alphabetical order based on subject. 
- Public Chat - Be able to interact with other users in Cheese Mail's public chatroom
- Recycle and Permanently Delete Messages - Be able to recycle, recover, and permantnly delete messages.
- Draft Messages - Be able to draft messages and send them at a later time.
- Attach Images - Add custom images to your messages.
- Custom Categories - Be able to add custom categories and categorize your messages.
- Edit user profile - Change your name, username, and password.
- View sent messages - View your sent messages.

## Requirements Completed 
- Ryan Pham - Login/Logout, Compose Messages, Delete User, Public Chatbox, Draft Messages
- Derrick Chan - Registration, Search Messages, and Attach Images
- Felix Vo - Sort Messages, Delete/Recycle Messages
- Marvin Xin - To-do List, Edit Profile, Custom Categories
- **EXTRA FEATURE (View Sent Messages)**: Done by Ryan Pham

## Project Status
Currently, our project has a total of 13 functional requirements completed that are implemented into our email client. We just added chatbox, recycle/delete messages, attach images to messages, custom categories, view sent messages, and edit user profile. We also completed some CSS styling as finishing touches.

## Acknowledgement
- Ryan Pham (@flotoria)
- Derrick Chan (@Dchan0621)
- Felix Vo (@JoeMamaBigison)
- Marvin Xin (@MarvinXin)

