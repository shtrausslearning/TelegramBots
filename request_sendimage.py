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

# Send multiple images to [chat_id] using [bot_id]

import requests
import time

base_url = "https://api.telegram.org/bot[bot_id]/sendPhoto"

# links to images
images = ["https1",
          "https2"]

descriptions = ['image1','image2']

# image send interval
intervals = 0.1

ii=-1
for image in images:
    ii+=1
    time.sleep(intervals)  
    parameters = {
      "chat_id" : "[chat_id]",
      "photo" : url,
      "caption" : descriptions[ii]}

  resp = requests.get(base_url,
                      data = parameters)
  print(resp.text)
