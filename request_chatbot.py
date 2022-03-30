# Utilising a dataset containing responses to user inputs in 
# [chat_id] bot [bot_id] will respond if the user input is found 
# in the dataset

# Example TSV file
# Question    Answer    Source    Metadata
# Hello    Hello	Dataset    editorial:data

import requests
import pandas as pd

url = 'tsv file'
df = pd.read_csv(url, sep="\t") # read dataset using tsv format
base_url = "https://api.telegram.org/bot[bot_id]"

def read_msg(offset):

  parameters = {
      "offset" : offset
  }

  resp = requests.get(base_url + "/getUpdates", data = parameters)
  data = resp.json()
  print(data)

  for result in data["result"]:
    send_msg(result)
  
  if data["result"]:
    return data["result"][-1]["update_id"] + 1

def auto_answer(message):
  answer = df.loc[df['Question'].str.lower() == message.lower()]  

  if not answer.empty:
      answer = answer.iloc[0]['Answer']
      return answer
  else:
      return "Cannot Understand User Input"

def send_msg(message):
  text = message["message"]["text"]
  message_id = message["message"]["message_id"]
  answer = auto_answer(text)

  parameters = {
      "chat_id" : "[chat_id]",
      "text" : answer,
      "reply_to_message_id" : message_id
  }

  resp = requests.get(base_url + "/sendMessage", data = parameters)
  print(resp.text)

offset = 0

# Continuously produce outputs
while True:  
  offset = read_msg(offset)
