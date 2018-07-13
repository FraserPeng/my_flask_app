
# title:接口header认证
# date:2018-7-5
# author:fraser

from flask_restful import Resource, abort
from model.api_param import header_param
from functools import wraps


def basic_authentication():
    header_par = header_param.header_par.parse_args()
    print("认证了--%s" % header_par)
    return True


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func)
        print(getattr(func, 'authenticated', True))
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)

        acct = basic_authentication()  # custom account lookup function

        if acct:
            return func(*args, **kwargs)

        abort(401)

    return wrapper


class Api_Resource(Resource):
    # method_decorators = [authenticate]
    super(Resource)
