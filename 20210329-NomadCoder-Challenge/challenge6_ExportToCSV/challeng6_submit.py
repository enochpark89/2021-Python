import os
import csv
import requests
from bs4 import BeautifulSoup
import io

"""
Plan:
1. Get the hyperlink from for the each grid - put them in the list
2. Using the list to get in to the hyperlink
3. Send requests to those pages - get the last number of the navigation.
4. Once we get the last number of the navigation, scrap all the job data from 1 to the last digit.
5. Export them in CSV file.
"""

os.system("clear")
alba_url = "http://www.alba.co.kr"

# Get the hyperlink of all the job postings.


def superbrand_page():
    request = requests.get(alba_url)
    soup = BeautifulSoup(request.text, 'html.parser')
    super_brand_jobs = soup.find("div", {"id": "MainSuperBrand"}).find(
        "ul", {"class": "goodsBox"}).find_all("li")
    return super_brand_jobs


def extract_job_info(html):
    jobs_info = []
    for job in super_brand_jobs:
        company_name = job.find("span", {"class": "company"}).string
        company_hyperlink = job.find("a")["href"]
        jobs_info.append({'company': company_name, 'link': company_hyperlink})
    return jobs_info


# Execution
super_brand_jobs = superbrand_page()

# Get a dictionary that contains the company name and the job info.
job_company_and_link = extract_job_info(super_brand_jobs)


def get_info_table(url):
    request = requests.get(url)
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


def save_to_file(name, table):
    try:
        with io.open(f'{name}.csv', "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["place", "title", "time", "pay", "date"])
            for row in table:
                writer.writerow([row[0], row[1], row[2], row[3], row[4]])
    except:
        print("failed to create", f'{name}')
    return

# Execution:


# Make a loop that iterate all jobs anc get information using the functions below:
for row in job_company_and_link:
    url = row["link"]
    company_name = row["company"]
    # Get a table that contains the information
    info_table = get_info_table(url)
    # Save each row into the csv file with the comapny_name
    save_to_file(company_name, info_table)
