from app.models import User
from app.db import Session, Base, engine

# Drop and rebuild tables
# Drops all existing tables
Base.metadata.drop_all(engine)
# Creates any tables that Base mapped in a class that inherits Base
Base.metadata.create_all(engine)

db = Session()

# Insert users
# Preps the SQL queries (doesn't actually add them)
db.add_all([
      User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
  User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
  User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='djiri4', email='gmidgley4@weather.com', password='password123'),
])

# Runs the actual SQL query
db.commit()

# Ends the CRUD operation interaction 
db.close()