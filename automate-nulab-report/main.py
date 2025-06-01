import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
APIKEY = os.getenv("API_KEY")
URL = f"https://nanaroq.backlog.jp/api/v2/issues/"

def get_count():
    count = f"count?apiKey={APIKEY}"
    finalUrl = URL + count
    print(finalUrl)
    r = requests.get(finalUrl)
    response = r.content.decode('utf-8')
    return json.loads(response).get('count')

def get_issue(issueIdOrKey):
    get_issue_url = f"{URL}{issueIdOrKey}?apiKey={APIKEY}"
    print(get_issue_url)
    r = requests.get(get_issue_url)
    return r.json()

info = get_issue("LABCI_OP-1")
print(json.dumps(info, indent=2, ensure_ascii=False))