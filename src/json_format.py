import json
from datetime import date
from decimal import Decimal
from sqlalchemy import create_engine, text
from config import configuration
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        if isinstance(o, date):
            return o.isoformat()
        return super().default(o)
engine = create_engine(configuration)
conn = engine.connect()
query = """
    SELECT o.name, cp.full_name, cp.phone, con.date, pay.contract_number, pp.payment_amount
    FROM contact_person AS cp
    JOIN organization AS o ON cp.id = o.id
    JOIN contracts AS con ON o.contract_id = con.id
    JOIN payments AS pay ON pay.contract_number = con.contract_number
    JOIN payment_plan AS pp ON con.id = pp.contract_id
    LEFT JOIN overpayment AS op ON pay.contract_number = op.contract_number
    WHERE pp.is_paid = 'false' AND con.is_valid = 'true' AND op.contract_number IS NULL
"""
result_proxy = conn.execute(text(query))
rows = result_proxy.fetchall()
columns = result_proxy.keys()
result = [dict(zip(columns, row)) for row in rows]
json_data = json.dumps(result, indent=4, cls=CustomJSONEncoder)
decoded_data = bytes(json_data, 'utf-8').decode('unicode_escape')
with open('send/debtors.json', 'w') as f:
    f.write(decoded_data)
print("JSON saved in send/debtors.json")
conn.close()