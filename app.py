from flask import Flask
from flask_restful import Api
from controller import client


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
if __name__ == '__main__':
    app.run(debug=True)
    # a = datetime.now()
    # print(a.timestamp())
