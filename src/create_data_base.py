from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine("*CONFIG THERE*")
Session = sessionmaker(bind=engine)
session = Session()

session.execute(text("INSERT INTO test VALUES ('2')"))
session.commit()

print("All done")

