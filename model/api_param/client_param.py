from flask_restful import reqparse

# 客户线索列表的查询条件
clue_list = reqparse.RequestParser()
clue_list.add_argument('agentId', type=int, required=True, help='经纪人id')
clue_list.add_argument('preId', type=int, required=False, help='线索列表第一行的id')
clue_list.add_argument('nextId', type=int, required=False, help='线索列表最后一行的的id')
clue_list.add_argument('status', type=int, required=False, help='线索状态')
clue_list.add_argument(
    'keyWord', type=str, required=False, help='关键字查询，姓名，手机号')


def task_status(value):
    statuses = [u"init", u"in-progress", u"completed"]
    return statuses.index(value)


# 推荐客户
clue_rec = reqparse.RequestParser()
clue_rec.add_argument(
    'name',
    type=str,
    required=True,
    help='客户名称',
    location='json',
    dest='client_name')
clue_rec.add_argument(
    'phone',
    type=str,
    required=True,
    help='客户手机号',
    location='json',
    dest='client_phone')
clue_rec.add_argument(
    'estateId',
    type=int,
    required=True,
    help='楼盘id',
    location='json',
    action='append',
    dest='estate_id')
clue_rec.add_argument(
    'agentId',
    type=int,
    required=True,
    help='经纪人id',
    location='json',
    dest='agent_id')
clue_rec.add_argument(
    'remark',
    type=str,
    required=False,
    help='推荐备注',
    location='json',
    dest='comment')
clue_rec.add_argument(
    'sex',
    type=int,
    required=False,
    default=1,
    help='性别',
    location='json',
    dest='gender')
clue_rec.add_argument(
    'saleCode',
    type=str,
    required=False,
    help='置业顾问',
    location='json',
    dest='sale_code')
clue_rec.add_argument(
    'status', type=task_status, required=False, help='状态', location='json')
