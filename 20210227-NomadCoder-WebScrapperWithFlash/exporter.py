import csv


def save_to_file(jobs):
    with open("jobs.csv", mode="w", newline='') as csvfile:
        writer = csv.writer(file)
        writer.writerow(["title", "company", "location", "link"])
        print(jobs)
        for job in jobs:
            writer.writerow(list(job.values()))
        return
