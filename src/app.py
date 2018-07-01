import os
import json
import mongodb
from flask import Flask, request

from module.Message import Message
from module.User import User
from process_message import process_message

dev_mode = os.getenv("PYTHON_DEV")

if dev_mode:
    import dotenv
    from pathlib import Path

    env_path = Path('../.env')
    dotenv.load_dotenv(env_path)

app = Flask(__name__)
app.config['MONGO_DBNAME'] = "py-chatible"
mongodb.mongo.init_app(app)


@app.route("/")
def index():
    return "Hello from my app"


@app.route("/message", methods=["POST"])
def receive_message():
    message_content = request.form['message']
    sender_id = request.form['messenger user id']

    sender = User(sender_id)
    message = Message(message_content)

    process_message(sender, message)
    return ""


@app.route("/media/<path:media_type>")
def send_image(media_type):
    return json.dumps({
        "messages": [
            {
                "attachment": {
                    "type": media_type,
                    "payload": {
                        "url": request.args.get('reply')
                    }
                }
            }
        ]
    })


@app.route("/register", methods=["POST"])
def register_user():
    form = request.form
    user_id = form['messenger user id']
    user_name = form['first name'] + form['last name']
    gender = form['gender']
    avatar = form['profile pic url']
    user = User(user_id)
    user.register(user_name, gender, avatar)
    return ""


if dev_mode == "true":
    app.run(port=3000)
