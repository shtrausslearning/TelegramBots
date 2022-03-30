# Using request library & url link to send a quiz/poll
# to [chat_id] using created bot[X] identifier

import requests
import json

base_url = "https://api.telegram.org/bot[X]/sendPoll"

parameters = {
    "chat_id" : "[chat_id]",
    "question" : "How much is 3+3?",
    "options" : json.dumps(['3','6','9']),
    "is_anonymous" : True,
    "type" : "quiz",
    "correct_option_id": 2,
    "explanation" : "Test Quiz"
}

resp = requests.get(base_url,data=parameters)
resp.json()
