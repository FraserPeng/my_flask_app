from app import db


class ClientClueInfo(db.Model):
    __tablename__ = 'client_clue_info'
    id = db.Column(db.Integer, primary_key=True)
    client_guid = db.Column(db.String(50), unique=True)
    client_name = db.Column(db.String(50))
    client_phone = db.Column(db.String(20), unique=True)
    gender = db.Column(db.Integer)
    estate_id = db.Column(db.Integer)
    rec_time = db.Column(db.DateTime)
    agent_id = db.Column(db.Integer)
    sale_code = db.Column(db.String(50))
    comment = db.Column(db.Text)
    status = db.Column(db.Integer)
    clue_mode = db.Column(db.Integer)
    clue_from = db.Column(db.Integer)
    expire_time = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean)
    df = db.Column(db.Boolean)
    create_by = db.Column(db.String(20))
    update_by = db.Column(db.String(20))
    create_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)

    def __init__(self, name, phone, estateId):
        self.client_name = name
        self.client_phone = phone
        self.estate_id = estateId

    def __repr__(self):
        return 'client_clue_info  %s  %s  %s  %s' % (
            self.client_name, self.client_phone, self.estate_id, self.rec_time)


class EstateInfo(db.Model):
    __tablename__ = 'estate_info'
    id = db.Column(db.Integer, primary_key=True)
    estate_name = db.Column(db.String(50))
    external_code = db.Column(db.String(50), unique=True)
    estate_type = db.Column(db.Integer)
    city_id = db.Column(db.Integer)
    df = db.Column(db.Boolean)
    create_by = db.Column(db.String(20))
    update_by = db.Column(db.String(20))
    create_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)

    def __init__(self, name, code, estateType, city):
        self.estate_name = name
        self.external_code = code
        self.estate_type = estateType
        self.city_id = city

    def __repr__(self):
        return 'estate_info  %s  %s  %s  %s' % (self.estate_name,
                                                self.external_code,
                                                self.estate_type, self.city_id)


class EstateCommissionRule(db.Model):
    __tablename__ = 'estate_commission_rule'
    id = db.Column(db.Integer, primary_key=True)
    estate_id = db.Column(db.Integer)
    house_class = db.Column(db.Integer)
    name = db.Column(db.String(200))
    city_id = db.Column(db.Integer)
    rule_code = db.Column(db.String(20), unique=True)
    rule_desc = db.Column(db.String(200))
    is_open = db.Column(db.Boolean)
    agent_types = db.Column(db.String(20))
    company_ids = db.Column(db.String(500))
    commission_mode = db.Column(db.Integer)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    df = db.Column(db.Boolean)
    create_by = db.Column(db.String(20))
    update_by = db.Column(db.String(20))
    create_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)

    def __init__(self, estateId, code, name):
        self.estate_id = estateId
        self.rule_code = code
        self.name = name

    def __repr__(self):
        return 'estate_commission_rule  %s  %s  %s  %s' % (
            self.name, self.rule_code, self.rule_desc, self.estate_id)


class EstateRecRule(db.Model):
    __tablename__ = 'estate_rec_rule'
    id = db.Column(db.Integer, primary_key=True)
    estate_id = db.Column(db.Integer)
    rule_code = db.Column(db.String(20), unique=True)
    rule_desc = db.Column(db.String(200))
    param = db.Column(db.String(20))
    is_open = db.Column(db.Boolean)
    agent_type = db.Column(db.Integer)
    err_msg = db.Column(db.String(100))
    df = db.Column(db.Boolean)
    create_by = db.Column(db.String(20))
    update_by = db.Column(db.String(20))
    create_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)

    def __init__(self, estateId, code, desc):
        self.estate_id = estateId
        self.rule_code = code
        self.rule_desc = desc

    def __repr__(self):
        return 'estate_rec_rule  %s  %s  %s  %s' % (
            self.desc, self.rule_code, self.rule_desc, self.estate_id)
