from sqlalchemy import *
from config import configuration
import os
engine = create_engine(configuration)
conn = engine.connect()
conn.execute(text(f'delete from debtors'))
conn.execute(text('drop view if EXISTS additional_info'))
file_path = 'send/debtors.json'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"The file '{file_path}' has been deleted.")
else:
    print(f"The file '{file_path}' does not exist.")
print("Clear debtors \nDelete view additional_info")

