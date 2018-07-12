from app import db


class AgentInfo(db.Model):
    __tablename__ = 'agent_info'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    name = db.Column(db.String(20))
    agent_type = db.Column(db.Integer)
    city_id = db.Column(db.Integer)
    telephone = db.Column(db.String(20))
    company_id = db.Column(db.Integer)
    register_time = db.Column(db.DateTime)
    register_channel = db.Column(db.Integer)
    referral_code = db.Column(db.String(20))
    status = db.Column(db.Integer)
    df = db.Column(db.Boolean)
    create_by = db.Column(db.String(20))
    update_by = db.Column(db.String(20))
    create_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)

    def __init__(self, account, phone, pwd):
        self.account = account
        self.telephone = phone
        self.password = pwd

    def __repr__(self):
        return 'client_clue_info  %s  %s' % (self.account, self.telephone)


