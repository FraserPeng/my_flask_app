from flask import Flask, got_request_exception
from flask_restful import Api
from controller import client

from config import logger
errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}

app = Flask(__name__)
api = Api(app, errors=errors, catch_all_404s=True)

api.add_resource(client.Clue,
                 '/clue/<int:id>', endpoint='clue')
api.add_resource(client.Clues, '/clue', endpoint='clues')


def log_exception(sender, exception, **extra):
    """ Log an exception to our logging framework """

    logger.info('系统错误详情：%s---其他：%s' % (exception, extra))


got_request_exception.connect(log_exception, app)

if __name__ == '__main__':

    app.run(debug=True)
