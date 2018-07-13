from domain.db_context import db
from datetime import datetime


class ClientClueInfo(db.Model):
    __tablename__ = 'client_clue_info'
    id = db.Column(db.Integer, primary_key=True)
    client_guid = db.Column(db.String(50))
    client_name = db.Column(db.String(50))
    client_phone = db.Column(db.String(20))
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


class CLientEstateCommissionRule(db.Model):
    __tablename__ = 'client_estate_commission_rule'
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
        return 'client_estate_commission_rule  %s  %s  %s  %s' % (
            self.name, self.rule_code, self.rule_desc, self.estate_id)


class ClientEstateRecRule(db.Model):
    __tablename__ = 'client_estate_rec_rule'
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


# -------------------------------以下是增删改查--------------------------------------


# --------------------线索相关---------------------
def add_clue(model: ClientClueInfo, is_commit=True):
    '''
    新增线索
    '''
    model.create_by = 'sys'
    model.create_date = datetime.now()
    model.df = 0
    db.session.add(model)
    if is_commit:
        db.session.commit()


def add_clue_list(data: list, is_commit=True):
    '''
    批量新增线索
    '''
    for model in data:
        model.create_by = 'sys'
        model.create_date = datetime.now()
        model.df = 0
        db.session.add(model)
    if is_commit:
        db.session.commit()


def update_clue_sale_code(sale_code: str, id: int, is_commit=True):
    '''
    更新置业顾问
    '''
    info = db.session.query(ClientClueInfo).filter_by(id=id).first()
    info.sale_code = sale_code
    if is_commit:
        db.session.commit()


def update_clue_expire_time(sale_code: str, id: int, is_commit=True):
    '''
    更新置业顾问
    '''
    info = db.session.query(ClientClueInfo).filter_by(id=id).first()
    info.sale_code = sale_code
    if is_commit:
        db.session.commit()


def update_clue_status(status: int, id: int, is_commit=True):
    '''
    更新状态
    '''
    info = db.session.query(ClientClueInfo).filter_by(id=id).first()
    info.status = status
    if is_commit:
        db.session.commit()


def get_clue_by_client_guid(client_guid: str):
    return db.session.query(ClientClueInfo).filter_by(
        client_guid=client_guid).first()


def get_clue_by_id(clueId: int):
    return db.session.query(ClientClueInfo).filter_by(id=id).first()


# --------------------线索相关--------------------------


def add_rec_rule(model: ClientEstateRecRule, is_commit=True):
    '''
    新增推荐规则
    '''
    model.create_by = 'sys'
    model.create_date = datetime.now()
    model.df = 0
    db.session.add(model)
    if is_commit:
        db.session.commit()


def add_rec_rule_list(data: list, is_commit=True):
    '''
    批量新增推荐规则
    '''
    for model in data:
        model.create_by = 'sys'
        model.create_date = datetime.now()
        model.df = 0
        db.session.add(model)
    if is_commit:
        db.session.commit()
