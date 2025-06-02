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
    project_id = 178803
    url = f"{base_url}?projectId[]={project_id}&apiKey={api_key}"
    print(url)
    response = requests.get(url).json()
    return len(response)

print(get_issue_list())