import requests
from bs4 import BeautifulSoup


# Get 'pagination' there are many titles by "1 of something; 2 of something etc"


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_pages = pages[-2].get_text(strip=True)
    return int(last_pages)


def extract_job(html):
    title = html.find("h2", {"class": "mb4"}).find("a")["title"]
    company, location = html.find(
        "h3", {"class": "fc-black-700"}).find_all("span", recursive=0)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip("\n")
    job_id = html['data-jobid']
    # 0=False, 1 = True
    return {'title': title, 'company': company, 'location': location, "apply_link": f"https://stackoverflow.com/jobs/{job_id}"}


def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page}")
        result = requests.get(f"{url}&pg={page+1}")
        # print(result.status_code) - to test the success rate of the request code.
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}&sort=i"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs
