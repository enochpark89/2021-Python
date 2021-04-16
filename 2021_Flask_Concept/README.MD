# Flask

-  Flask is a Micro-framework for Python.

## 1. Route

-  When you set the route, it will take the user to the designated patge.

```python
import requests
from flask import Flask, render_template, request
import json

app = Flask("DayElevenApp")

@app.route("/")
def home():
  return "I am home!"

app.run(host="0.0.0.0")
```

-  this short code returns "I am home!" in the home page(host=0.0.0.0)

## 2. Beautiful Soup

-  BeautifulSoup library allows you to get the HTML tags and content from the website.

```python
import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import json

# start an app
app = Flask("DayElevenApp")

# request for the URL on a website page
reddit_url= "https://www.reddit.com/r/javascript/top/?t=month/"
request = requests.get(reddit_url)

# BeautifulSoup() will convert html file into text.
soup = BeautifulSoup(request.text, 'html.parser')

# A variable soup now has all the html tags from the website.
print(soup.prettify())

@app.route("/")
def home():
  return

app.run(host="0.0.0.0")
```

04/08/2021
- list can be added using (list1+list2): same as merge
- sorting
  *list[dictionary]
  
```python
[{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
from operator import itemgetter
newlist = sorted(list_to_be_sorted, key=itemgetter('name')) 
```