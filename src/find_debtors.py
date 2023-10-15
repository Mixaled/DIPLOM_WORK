from sqlalchemy import *
from config import configuration
engine = create_engine(configuration)
conn = engine.connect()
query_additional_info = """
select  o.name, cp.full_name, cp.phone, con.date, pay.contract_number, pp.payment_amount
from contact_person as cp 
join organization as o
on cp.id = o.id 
join contracts as con 
on o.contract_id = con.id
join payments as pay
on pay.contract_number = con.contract_number
join payment_plan as pp
on con.id = pp.contract_id 
left join overpayment AS op 
ON pay.contract_number = op.contract_number
where pp.is_paid ='false' and con.is_valid = 'true' and op.contract_number is NULL
"""
query_update_deb = """
insert into debtors (organization, amount, number, date)
select o.name as organization, pp.payment_amount as amount, cp.phone as number, con.date as date
from contact_person as cp 
join organization as o
on cp.id = o.id 
join contracts as con 
on o.contract_id = con.id
join payments as pay
on pay.contract_number = con.contract_number
join payment_plan as pp
on con.id = pp.contract_id 
left join overpayment AS op 
ON pay.contract_number = op.contract_number
where pp.is_paid ='false' and con.is_valid = 'true' and op.contract_number is NULL;
"""
view = f"create view additional_info as ({query_additional_info})"
conn.execute(text(view))
conn.execute(text(query_update_deb))
print("View updated\nDebtors updated")
