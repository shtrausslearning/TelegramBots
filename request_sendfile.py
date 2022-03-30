# Send [my_file] to Telegram Chat [chat_id] using bot [bot_id]

import requests
import time

base_url = "https://api.telegram.org/bot[bot_id]/sendDocument"

my_file = open("/kaggle/input/filter-spectogram-images/afrsil1/XC125458_0.npy", "rb")

parameters = {
    "chat_id" : "[chat_id]",
    "caption" : "description"
}

files = {
    "document" : my_file
}

resp = requests.get(base_url,
                    data = parameters,
                    files=files)
print(resp.text)
