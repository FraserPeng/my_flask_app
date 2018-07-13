'''
title:header认证参数
date:2018-7-5
author:fraser
'''

from flask_restful import reqparse


# 客户线索列表的查询条件
header_par = reqparse.RequestParser()
header_par.add_argument('session-key', type=str,
                        required=True, location='headers', help='认证失败，没有认证参数')
