from app import app
from app import socketio
app.run(debug=True)
socketio.run(app, host="localhost")