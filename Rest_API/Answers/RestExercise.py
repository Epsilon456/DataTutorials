import requests
import json
import pandas as pd

# Set these variables to your filepaths
USERS_FILE = "[PATH TO THE GITUSERS.TXT FILE]"
OUTPUT_FILE_NAME = "[PATH TO SAVE THE OUTPUT]"

#The base url for the github api
URL_BASE = "https://api.github.com/users/"

# Read file as a string of text
with open(USERS_FILE,'r') as f:
    file_text = f.read()

# Since each user is separated by a carriage return, we can split the text by "\n" (the new line character) to break
    # it into a list.
users = file_text.split("\n")

#Create a dictionary to store the output. Each value of the dictionary is an empty list.
output = {"username":[], "date_made":[], "num_repos":[]}
for user in users:
    #construct the url and get the response
    url = URL_BASE+user
    response = requests.get(url)
    dictionary = json.loads(response.text)

    # Get the desired fields from the dictionary and append them to the appropriate list within the dictionary.
    output["username"].append(dictionary['login'])
    output["date_made"].append(dictionary['created_at'])
    output["num_repos"].append(dictionary['public_repos'])

df = pd.DataFrame(output)
df.to_csv(OUTPUT_FILE_NAME,index=False)



