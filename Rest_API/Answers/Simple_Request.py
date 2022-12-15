import requests
import json
url = "https://api.github.com/users/epsilon456"
response = requests.get(url)
dictionary = json.loads(response.text)

username = dictionary['login']
date_made = dictionary['created_at']
num_repos = dictionary['public_repos']

print(username, date_made, num_repos)