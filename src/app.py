import dotenv
import json
from flask import Flask, request
from pathlib import Path
from api.send_message import send_message

env_path = Path('../.env')
dotenv.load_dotenv(env_path)

app = Flask(__name__.split('.')[0])


@app.route("/")
def index():
    return "Hello from my app"


@app.route("/message", methods=["POST"])
def receive_message():
    message = request.form['message']
    sender_id = request.form['messenger user id']
    send_message(sender_id, message)
    return ""


@app.route("/media/<path:media_type>")
def send_image(media_type):
    return json.dumps({
        "messages": [
            {
                "attachment": {
                    "type": media_type,
                    "payload": {
                        "url": request.args.get('media_url')
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
    return ""
