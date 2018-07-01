import requests
import os

block_id = {
    "text": os.getenv('TEXT_BLOCK_ID'),
    "video": os.getenv('VIDEO_BLOCK_ID'),
    "image": os.getenv('IMAGE_BLOCK_ID'),
    "audio": os.getenv('AUDIO_BLOCK_ID')
}


def send(recipient_id, message):
    url = 'https://api.chatfuel.com/bots/{}/users/{}/send?chatfuel_token={}&chatfuel_block_id={}'.format(
        os.getenv('BOT_ID'), str(recipient_id), os.getenv('SEND_TOKEN'), block_id[message.type])
    data = {
        "reply": message.content
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        raise Exception("Request error", response.text)
