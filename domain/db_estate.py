from app import db


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

