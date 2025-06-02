import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
base_url = "https://nanaroq.backlog.jp/api/v2/issues"

def get_count():
    url = f"{base_url}/count?apiKey={api_key}"
    print(url)
    response = requests.get(url).content.decode("utf-8")
    return json.loads(response).get("count")

def get_issue(issue_id_or_key):
    url = f"{base_url}/{issue_id_or_key}?apiKey={api_key}"
    print(url)
    return requests.get(url).json()

def get_issue_list():
    params = {
        "apiKey" : api_key,
        "projectId[]": 178803,
        "count": 100,
        "offset" : 0
    }
    all_issues = []

    while True:
        response = requests.get(base_url, params=params)
        issues = response.json()
        if not issues:
            break
        all_issues.extend(issues)
        params["offset"] += 100

    return len(all_issues)

print(get_issue_list())