
from flask_restful import fields
from datetime import datetime


class expire_time_format(fields.Raw):
    def format(self, value):
        if(isinstance(value, datetime)):
            pass
        if value:
            return '1111111'
        else:
            return '-----'


status_str = {0: '审核中', 1: '推荐中', 2: '来电',
              3: '到访', 4: '认筹', 5: '认购', 6: '签约', 7: '回款'}


class status_format(fields.Raw):
    def format(self, value):
        if not value:
            return '-----'
        else:
            return status_str[value]


clue_list = {
    'clueId':   fields.Integer(attribute='id'),
    'req_url':   fields.Url(absolute=True),
    'recTime': fields.DateTime,
    'status': status_format(),
    'name': fields.String,
    'phone': fields.String,
    'estateName': fields.String,
    'expireDay': fields.Integer(attribute='expire_time'),
}
