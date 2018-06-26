import requests
import os


def send_image(recipient_id, media_url):
    url = 'https://api.chatfuel.com/bots/{}/users/{}/send?chatfuel_token={}&chatfuel_block_id={}'.format(
        os.getenv('BOT_ID'), str(recipient_id), os.getenv('SEND_TOKEN'), os.getenv('IMAGE_BLOCK_ID'))
    data = {
        "media_url": media_url
    }
    response = requests.post(url, json=data)
    if response.status_code != 200:
        raise Exception("Request error", response.text)
