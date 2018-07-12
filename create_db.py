from app import db
from domain import db_agent,db_client,db_estate
db.drop_all()
db.create_all()