import requests
from config import site
with open('send/debtors.json', 'r') as f:
    debtors_json = f.read()
ats_url = site
headers = {'Content-Type': 'application/json'}
response = requests.post(ats_url, data=debtors_json, headers=headers)
