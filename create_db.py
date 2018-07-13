
from domain import db_agent, db_client, db_estate,db_context
db_context.db.drop_all()
db_context.db.create_all()