# Create a Poll in group [chat_id] using [bot_id] & extract and plot results
# Using Plotly Express

import requests
import json
import plotly.express as px

base_url = "https://api.telegram.org/bot[bot_id]/sendPoll"

parameters = {
    "chat_id" : "[chat_id]",
    "question" : "How much is 3+3?",
    "options" : json.dumps(['3','6','9']),
    "is_anonymous" : True,
    "allows_multiple_answers" : True,
    "type" : "regular",
    "explanation" : "Test Poll"
}

resp = requests.get(base_url,data=parameters)
resp.json() # show request content

# Get Show all Updates for Bot Interactions
# Eg. if bot is located in group, updates will contain group(chat_id) data
base_url = "https://api.telegram.org/bot[bot_id]/getUpdates"

parameters = {
    "offset" : "offset_id"
}

resp = requests.get(base_url,
                    data=parameters)
# list of all updates
lst_updIDs = resp.json()['result'] 

# show poll results

# Select the desired poll update
options = lst_updIDs[-4]['poll']['options']

# Store Data in lists
lst_res = []; lst_options = []
for i in options:
    option = i['text']
    votes = i['voter_count']
    lst_res.append(votes)
    lst_options.append(option)
   
# Plot results
px.bar(x=lst_options,y=lst_res)
