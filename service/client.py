from domain.db_context import db
from domain import db_client
from datetime import datetime
from flask_restful import abort
from common import helper, enums


class ClientService(object):
    def add_clue(self, **kw):
        '''
        推荐楼盘
        '''
        print(kw)
        is_multi_estate = True
        if helper.dict_key_is_empty('client_name', kw):
            abort(405, err_msg='客户姓名不能为空')
        if helper.dict_key_is_empty('agent_id', kw):
            abort(405, err_msg='经纪人不能为空')
        if helper.dict_key_is_empty('client_phone', kw):
            abort(405, err_msg='客户手机号码不能为空')
        if helper.dict_key_is_empty('estate_id', kw):
            abort(405, err_msg='推荐楼盘不能为空')
        estate_ids = kw['estate_id']
        if len(estate_ids) == 1:
            is_multi_estate = False
        if is_multi_estate:
            for estate_id in estate_ids:
                self.__put_clue(estate_id, is_commit=False, **kw)
            db.session.commit()
        else:
            self.__put_clue(kw['estate_id'], **kw)

    def __put_clue(self, estateId, is_commit=True, **kw):
        model = db_client.ClientClueInfo(kw['client_name'], kw['client_phone'],
                                         estateId)
        model.rec_time = datetime.now()
        model.gender = kw.get('gender', 1)
        model.sale_code = kw.get('sale_code', None)
        model.agent_id = kw['agent_id']
        model.comment = kw.get('comment', None)
        model.status = enums.clue_status_enum.auditing.value
        model.is_valid = True
        model.clue_from = kw.get('clue_from',
                                 enums.clue_belong_enum.share.value)
        model.clue_mode = kw.get('clue_mode', enums.clue_mode_enum.alls.value)
        db_client.add_clue(model, is_commit)
