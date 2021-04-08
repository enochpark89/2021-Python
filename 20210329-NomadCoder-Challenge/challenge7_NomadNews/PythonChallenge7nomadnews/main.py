import requests
from flask import Flask, render_template, request
import json


base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api


def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}
app = Flask("DayNine")
articles = []


def get_info():
    num = 1
    for hit in hits:
        if (
            (hit['created_at'] == "NONE" or hit['created_at'] == None)
            or (hit['title'] == "NONE" or hit['title'] == None)
            or (hit['url'] == "NONE" or hit['url'] == None)
            or (hit['points'] == "NONE" or hit['points'] == None)
            or (hit['author'] == "NONE" or hit['author'] == None)
            or (hit['num_comments'] == "NONE" or hit['num_comments'] == None)
        ):
            continue
        else:
            dict = {
                '#': num,
                'created_at': hit['created_at'],
                'title': hit['title'],
                'url': hit['url'],
                'points': hit['points'],
                'author': hit['author'],
                'num_comments': hit['num_comments']
            }
            articles.append(dict)
            num += 1


@app.route("/")
def home():
    return render_template("index.html", articles=articles, len=len(articles))


@app.route("/News")
def home():


app = Flask(__name__)
