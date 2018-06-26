import requests
import os


def send_text(recipient_id, message):
    url = 'https://api.chatfuel.com/bots/{}/users/{}/send?chatfuel_token={}&chatfuel_block_id={}'.format(
        os.getenv('BOT_ID'), str(recipient_id), os.getenv('SEND_TOKEN'), os.getenv('TEXT_BLOCK_ID'))
    data = {
        "reply": message
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        raise Exception("Request error")
