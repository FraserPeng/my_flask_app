from app import db
from domain import db_context
db.drop_all()
db.create_all()