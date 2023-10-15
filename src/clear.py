from sqlalchemy import *
from config import configuration
import os
engine = create_engine(configuration)
conn = engine.connect()
conn.execute(text(f'delete from organization'))
conn.execute(text(f'delete from contact_person'))
conn.execute(text(f'delete from contracts'))
conn.execute(text(f'delete from payments'))
conn.execute(text(f'delete from overpayment'))
conn.execute(text(f'delete from payment_plan'))
conn.execute(text(f'delete from org_person'))
print("All clear (except debtors)")