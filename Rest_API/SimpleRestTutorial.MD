# Simple Rest API

API stands for "Application Programming Interface". This is a convenient way for a 
program to interact with a web server. Typically, you will interact with an API through a web interface. For example, 
Github has an API that you can use to get information on different users.  Let's see what it says about me.

Try going to this URL and see what information you can get about my Github.
```buildoutcfg
https://api.github.com/users/epsilon456
```

When you hit that url, you should see something like this:
```buildoutcfg
{
  "login": "Epsilon456",
  "id": 11969091,
  "node_id": "MDQ6VXNlcjExOTY5MDkx",
  "avatar_url": "https://avatars.githubusercontent.com/u/11969091?v=4",
 ...
}
```
So what just happened?  When you visited the url, you sent a request to Github's server. The server then sent you a response.
The format the the response is in is called JSON. 

Many API's, are REST API's like this one.  They receive an HTTP method and return a JSON.
Try replacing my username with another Github user and you will get the appropriate JSON for that person. 

```buildoutcfg
https://api.github.com/users/visionmedia
```
When you use this HTTP request, you will get another json formatted the exact same way.

## JSON and Dictionaries
A JSON file is practically identical to a python dictionary.  I will explain the subtle differences in a moment.

#### Key
A python dictionary will contain a set of key:value pairs contained inside curly brackets.  The key will be some index 
that you want to use to look-up information and must be an unmutable (unchangeable) type such as an int or string.  (Keys
cannot be floats or lists).
#### Value
The value section of a python dictionary can be practically anything (even floats, lists, classes, or other dictionaries).

#### Example
In Python, you will usually use dictionaries to map one value to another. Here we will define a dictionary of superhero 
aliases. The key for each item (key:value pair) in the dictionary will be the superhero name and the secret identity will 
be the value.  We can separate items with commas and add as many as we want.  Remember that each item is a key-value pair.
In our example, both the key and the value are strings so you will need to put quotes around each key and each value.
```buildoutcfg
aliases = {"Iron Man":"Tony Stark", "Captain America":"Steve Rogers", "Black Widow":"Natasha Romanoff"}
```
In a Python dictionary, we can pass a key to the dictionary by putting it in square brackets like this:

```buildoutcfg
print(aliases["Iron Man"])
```

Once our dictionary is defined, we can continue to add items to it:
```buildoutcfg
aliases["Spider Man"] = "Peter Parker"
```

Remember, we can also use dictionaries to store numbers like this: 
```buildoutcfg
constants = {"pi":3.14159,"e":2.718,"c":2.9978E8}
print(constants["c"])
```
...Or other dictionaries like this:
```buildoutcfg
my_dictionaries = {"aliases":aliases,"constants":constants}
print(my_dictionaries["aliases"])
```
Notice that in all of these examples, the key was a string.  Strings and integers are, by far, the most common
keys to use for dictionaries.  Also notice how, when I defined "my_dictionaries", I used quotes around the key, but not 
for the value.  This is because the key is a string, and the value is a dictionary in that example.

### Note: The difference between JSON and Dictionaries
JSON's and Python dictionaries are formatted the same way, however, their difference is on how they work underneath.  At 
the moment, you don't need to be aware of this difference, but the difference is interesting and will come in handy later on.

A JSON file is simply a text file that is used to tie keys and values together. A Dictionary on the other hand has some internal
processes that make looking up information extremely efficient.  Dictionaries are essentially the same as Hashmaps in Java. 
When you define a dictionary, Python will create a function under the hood that ties the name of your key to the physical memory
address in your machine's RAM.  This means that, when you look up a "Iron Man", Python isn't doing a string search for "Iron Man".  
Instead, it passes that string to an internal function that maps it to the memory address that contains the value "Tony Stark".
This means that it doesn't have to search through the entire dictionary.  As a result, the time it takes to lookup a value 
does not depend on the size of the dictionary.  A dictionary with 10 values will be just as fast as one with 10,000,000 values!

While that is a complicated explaination for what a Dictionary is, there are two key takeaways that are important to remember:
1) Each key must be unique.  (Since a key goes to a memory address you cannot have multiple entries for "Tony Stark".)
2) JSON is text and a Dictionary is its own data type. The good news is that Python can easily convert between the two 
since they are in the same format.

## Tying it back to JSON
Take a look at the file "TV_shows" in this folder.  This is essentially a spreadsheet in JSON format.
Notice that each key corresponds to a column name and each value is a list.

If you import the python json library (which is standard and should not need to be installed), you can easily
open it as a dictionary with the code below.
```buildoutcfg
import json
with open("TV_shows.json",'r') as f:
    dictionary = json.load(f)
```
The pandas dataframe allows you to convert the dictionary into a dataframe so that it looks like a spreadsheet again:
```buildoutcfg
import pandas as pd
df = pd.DataFrame(dictionary)
```

## REST Requests
Now that we have gone through what JSON is, let's tie it back to REST. We want to be able to send an HTTP request
to a server and then receive a JSON file that we can add to a spreadsheet.

Before we obtained the request by typing "https://api.github.com/users/epsilon456
 into the url, but let's do it programatically.  To do this, we use Python's requests library.
 
If you do not have this installed, open your Anaconda terminal and run 
```buildoutcfg
pip install requests
```
This library contains a function called "get" that allows you to pass a URL and will return a response.
The response will have some metadata attached to it, but what we are interested in is "response.txt"

You can use the code below to send the request with the url and print the JSON response.
```buildoutcfg
import requests
url = "https://api.github.com/users/epsilon456"
response = requests.get(url)
print(response.text)
```

### A Note on JSON Format.
There are 3 different things that use the JSON format that are subtly different.  
1) A Python dictionary object.  This is a native Python datatype that you can reference using: "dictionary[key]" Typically, 
in your Python code, you will want to work with information in this format as a dictionary.
2) A JSON object.  This is a file type.  If the file is saved on your desktop, it will have the ".json" extention.  
3) A JSON string.  This is a text representation of the file.  For example, the "TV_shows.json" file can be represented by the
following text string:
```buildoutcfg
string = '{"Show": ["Bee and Puppycat","Andor","Mythic Quest","Sherlock"],"Rating": [8.2,8.4,7.8,9.1],"Seasons": [2,1,3,4]}'
```
If you want to convert the text string into a dictionary, you will want to use the "json.loads" function. (The "s" stands 
for "string") 

```buildoutcfg
import json
dictionary = json.loads(string)
```

## Using JSON Data
Now that we know that "requests.text" is a string, we can convert it to a Python dictionary using:
```buildoutcfg
import json
dictionary = json.loads(response.text)
```

Let's print specific parts from this dictionary.  Let's find my username, the date I created my account, and the number of 
repos that I have.  
```buildoutcfg
username = dictionary['login']
date_made = dictionary['created_at']
num_repos = dictionary['public_repos']

print(username, date_made, num_repos)
```

You did it!  You have successfully made an API request and parsed the resulting JSON response.

## Code
If you want to see the full code altogether, take a look at /Rest_API/Answers/Simple_Request.py

## Exercise
Now that we got one finished, let's programically extract the same fields for a list of git users.
The usernames of the top 10 Github accounts are listed in the file "GitUsers.txt"
Use the Github API to find the "login", "created_at", and "public_repos" for all 10 users and export them to a .csv file.

If you get stuck, take a look at /Rest_API/Answers/RestExercise.py

## Wrapping up
Each API is different.  Othe API's will differ slightly in how you need to pass the url and what keys are returned in the 
JSON response.  

What's nice about the github API is that you can access it for free (the free api limits you to 
60 requests per hour).  Some API's will require you to use an authentication token in order to make requests (which is a 
job for a different tutorial)

## Further Reading
https://realpython.com/api-integration-in-python/