import requests
from config import configuration, site
from sqlalchemy import *
engine = create_engine(configuration)
conn = engine.connect()
url = site
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for item in data:
        name = item["name"]
        full_name = item["full_name"]
        phone = item["phone"]
        date = item["date"]
        contract_number = item["contract_number"]
        payment_amount = item["payment_amount"]
        is_paid = item["is_paid"]
        if is_paid:
            conn.execute(text(f"delete from debtors where name = :name"), name=name)
            conn.execute(text(f"update payment_plan set is_paid = 'true'"))
else:
    print(f"ERROR: {response.status_code}")
