from api.send_message import send_message
from module.Message import Message
from module.User import User, pair, unpair


def process_message(user: User, message: Message):
    if user.status == "inactive":
        send_message(user.user_id, "Started Pairing")
        pair(user)
        pass
    elif user.status == "pending":
        send_message(user.user_id, "Đợi 1 lúc nữa")
    elif message.content.lower() == "glhf":
        unpair(user)
        pass
    else:
        send_message(user.partner, message)
