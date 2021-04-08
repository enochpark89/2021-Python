
"""
2.14 What is CSV?
A file that has the data seperated by comma.
What are ways to get access to csv file?
1. Google Spreadsheet
2. Excel
3. Python has csv build in.

import csv
ex:


def save_to_file(jobs):
    # There are mode to open the file. you can Read or Write.
    file = open("jobs.csv", mode="w")

    # Writer is going to write the headers: take the file and start writing
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])

    # Job returns a dictionary with four values for the course.
    for job in jobs:
        # Dictioanry can call the value in it. list() will return all the value as a list.
        print(list(job.value()))

    return


"""
import os
import csv
import requests
from bs4 import BeautifulSoup
import re
import io


kumon_url = 'http://kumon.alba.co.kr/'


def get_info_table(url):
    request = requests.get(kumon_url)
    soup = BeautifulSoup(request.text, 'html.parser')
    normal_info = soup.find("div", {"id": "NormalInfo"})
    tr_tables = normal_info.find(
        "table", {"cellspacing": "0"}).find("tbody").find_all("tr")
    info_table = []
    for row in tr_tables:
        try:
            place = row.find("td", {"class": "local"}).text
            place = place.replace('\xa0', ' ')
            title = row.find("td", {"class": "title"}).find(
                "a").find("span", {"class": "company"}).string
            time = row.find("td", {"class": "data"}).text
            pay = row.find("td", {"class": "pay"}).text
            date = row.find("td", {"class": "regDate last"}).text
        except:
            continue
        info_table.append([place, title, time, pay, date])
    return info_table


def save_to_file(table):
    with io.open("jobs.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["place", "title", "time", "pay", "date"])
        for row in table:
            writer.writerow([row[0], row[1], row[2], row[3], row[4]])
    return


info_table = get_info_table(kumon_url)
save_to_file(info_table)
