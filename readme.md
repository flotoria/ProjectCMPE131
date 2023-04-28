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
pip install datetimes
pip install wtforms
```

Initialize the database
``` 
python
from app import db
from app import app
app.app_context().push()
db.create_all()
exit()
``` 
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
Python version: 3
Html:
flask: login, sqlalchemy, wtf
werkzeug security
datetimes
wtforms

## How to use
Start by registering for a new account which will be stored in the database. Then you will be prompted into signing in with the information you have provided. Once that is completed you will reach the dashboard where there are 5 different buttons.


From there depending on which button you press, you will be taken to different parts of the website which will prompt users to enter the following information to do the specific requirement. The five buttons consist of Logout, Compose, Delete, Search, Sort, and To-Do which corresponds to the different functional requirements implemented in the application.

## List of Features
- Logout - Selecting this button will log you out of the current account that you are using
- Compose - Selecting this button will bring you into the page for composing a message and from there you would have to input a receiving user, subject of the message, and body to be able to send a message to another user
- Delete - Pressing the delete button will delete the user account that you are currently using and get rid of the information inside the database. 
- Search - Pressing the search button will allow you to search through the messages that have been sent to you that can be filteted by matching words inside the body and subject. 
- To-Do - Selecting the To-Do button will allow the user to create a to-do list of tasks that want to accomplish and when they are finished, they can mark it as done.
- Sort - Selecting the Sort button will allow user to interact with a drop-down bar that can sort the messages in the user's inbox by time and by alphabetical order based on subject. 

## Requirements Completed 
- Ryan Pham - Login/Logout, Compose Messages, and Delete User
- Derrick Chan - Registration and Search Messages
- Felix Vo - Sort Messages
- Marvin Xin - To-do List

## Project Status
Currently, our project has a total of 8 functional requirements completetd that are implemeted into our email client. We still have 4 other functional requirements that will needto be implemented including a chatbox, categorizing emails, edit user profile, and a new functional requirement that is still to be determined. Also, our application doesn't have any CSS styling incorporated with it and is primarily focused on functionality and having all the features work smoothly. 

## Acknowledgement
- Ryan Pham (@flotoria)
- Derrick Chan (@Dchan0621)
- Felix Vo (@JoeMamaBigison)
- Marvin Xin (@MarvinXin)

