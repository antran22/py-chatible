from .sender import send
from module.Message import Message


def send_message(recipient_id: int, message):
    if not isinstance(message, Message):
        message = Message(message)
    send(recipient_id, message)