from flask_restful import marshal_with, Resource
from api_param import client_param
from api_resp import resp_client
from controller import base


class Clue(base.Api_Resource):
    '''
    线索
    '''

    def __init__(self):
        pass

    def get(self, id):
        args = client_param.clue_list.parse_args()
        return {'id': id, 'args': args}


class Clues(Resource):
    @marshal_with(resp_client.clue_list, envelope='data')
    def get(self):
        args = client_param.clue_list.parse_args()
        return {'args': args, 'flags': True, 'status': None}

    def post(self):
        args = client_param.clue_rec.parse_args()
        return {'args': args}
