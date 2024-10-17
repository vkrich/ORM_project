import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = db.create_engine('sqlite:///alchemy_users.db')
conn = engine.connect()
metadata = db.MetaData()

users = db.Table('users', metadata, 
  db.Column('user_id', db.Integer, primary_key=True),
  db.Column('user_name', db.Text),
  db.Column('user_age', db.Integer)
)

# Create the table in the database
metadata.create_all(engine)

insertion_query = users.insert().values([
    {'user_name': 'Vasya', 'user_age': 17},
    {'user_name': 'Petr', 'user_age': 25},
    {'user_name': 'Fedya', 'user_age': 18},
    {'user_name': 'Ivan', 'user_age': 23},
])

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

session.execute(insertion_query)
session.commit()

update_query = db.update(
        users
    ).where(
        users.columns.user_name=='Vasya'
    ).values(user_age=19)
session.execute(update_query)
session.commit()

session.execute(
    db.delete(
        users
    ).where(
        users.columns.user_name=='Vasya'
    )
)
session.commit()

select_all_results = session.execute(
    db.select([users]).where(users.columns.user_age > 18)
)

for user in select_all_results.fetchall():
    print(user)

# Close the connection
session.close()
