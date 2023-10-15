import random
from sqlalchemy import *
from config import configuration
from names import organizations, INN, men_names, men_surnames, men_third, women_names, women_surnames, women_third
import names
from datetime import datetime, timedelta
engine = create_engine(configuration)
conn = engine.connect()

for i in range(150):
    organization_name = random.choice(organizations)
    query = text(f'INSERT INTO organization (id, name, contract_id, inn) '
                 f'VALUES ({i}, \'{organization_name}\', {i}, {INN[i]})')
    conn.execute(query)
for i in range(150):
    phone_n = names.random_phone()
    rand_sex = random.choice(["m", "f"])
    if rand_sex == "m":
        id_list = random.sample(range(150), 150)
        rand_name = random.choice(men_surnames) + " " + random.choice(men_names) + " " + random.choice(men_third)
        query = text(f'INSERT INTO contact_person (id, org_id, full_name, phone) '
                     f'VALUES ({i}, \'{id_list[i]}\',\'{rand_name}\', \'{phone_n}\')')
        conn.execute(query)
    if rand_sex == "f":
        id_list = random.sample(range(150), 150)
        rand_name = random.choice(women_surnames)+ " " + random.choice(women_names) + " " + random.choice(women_third)
        query = text(f'INSERT INTO contact_person (id, org_id, full_name, phone) '
                     f'VALUES ({i}, \'{id_list[i]}\',\'{rand_name}\', \'{phone_n}\')')
        conn.execute(query)

contract_numbers = random.sample(range(100000000, 999999999 + 1), 150)

start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 6, 7)

for i in range(150):
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    random_bool = random.choice([True, False])
    query = text(f"INSERT INTO contracts (id, is_valid, contract_number, date) "
                 f"VALUES ({i}, {random_bool}, '{contract_numbers[i]}', '{random_date}')")
    conn.execute(query)

for i in range(150):
    year = random.randint(2020, 2023)
    month = random.randint(1, 8)
    day = 17
    date = datetime(year, month, day)
    formatted_date = date.strftime("%d.%m.%Y")
    query = text(f"INSERT INTO payments (actual_payment_id, contract_number, payment_amount, inn, payment_date) "
                 f"VALUES ({i}, '{contract_numbers[i]}', {round(random.uniform(0, 9999999.99), 2)}, {INN[i]}, '{formatted_date}')")
    conn.execute(query)

for i in range(20):
    year = random.randint(2020, 2023)
    month = random.randint(1, 8)
    day = 17
    date = datetime(year, month, day)
    formatted_date2 = date.strftime("%d.%m.%Y")
    id_list = random.sample(range(150), 150)
    query = text(f"INSERT INTO overpayment (actual_payment_id, contract_number, additional_funds, inn, payment_date) "
                 f"VALUES ({i}, '{contract_numbers[id_list[i]]}', {round(random.uniform(0, 9999999.99), 2)}, {INN[i]}, '{formatted_date2}')")
    conn.execute(query)

for i in range(150):
    random_bool = random.choice([True, False])
    contract_id = conn.execute(text("SELECT id FROM contracts")).fetchall()[i][0]
    payment_id = conn.execute(text("SELECT actual_payment_id FROM payments")).fetchall()[i][0]
    payment_amount = conn.execute(text("SELECT payment_amount FROM payments")).fetchall()[i][0]
    payment_date = conn.execute(text("SELECT payment_date FROM payments")).fetchall()[i][0]
    contract_date = conn.execute(text("SELECT date FROM contracts")).fetchall()[i][0]
    query = text(
        f"INSERT INTO payment_plan "
        f"VALUES ({contract_id}, {payment_id}, '{payment_amount}', '{payment_date}', '{contract_date}', {random_bool})"
    )
    conn.execute(query)
for i in range(150):
    contact_id = conn.execute(text("SELECT id FROM contact_person")).fetchall()[i][0]
    organization_id = conn.execute(text("SELECT id FROM organization")).fetchall()[i][0]
    query = text(
        f"INSERT INTO org_person "
        f"VALUES ({contact_id}, {organization_id})"
    )
    conn.execute(query)
print("All done")











