import csv
import os

def save_results(results, file_path="data/leads.csv"):
    os.makedirs("data", exist_ok=True)

    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "company_name",
            "website",
            "snippet",
            "emails",
            "analysis",
            "score",
            "outreach"
        ])
        if not file_exists:
            writer.writeheader()

        for row in results:
            writer.writerow(row)