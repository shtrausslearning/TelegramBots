# Send an image to [chat_id] using [bot_id]

import requests
import time

base_url = "https://api.telegram.org/bot[bot_id]/sendPhoto"

parameters = {
    "chat_id" : "[chat_id]",
    "photo" : "[image https]",
    "caption" : "description"
}

resp = requests.get(base_url, data = parameters)
print(resp.text)
