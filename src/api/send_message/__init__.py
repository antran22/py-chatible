from .content_type import determine_content_type
from .send_text import send_text
from .send_image import send_image
from .send_video import send_video
from .send_audio import send_audio


def send_message(recipient_id, message):
    message_type = determine_content_type(message)
    # print(message + " of type " + message_type)
    if message_type == "text":
        send_text(recipient_id, message)
    elif message_type == "image":
        send_image(recipient_id, message)
    elif message_type == "video":
        send_video(recipient_id, message)
    else:
        send_audio(recipient_id, message)