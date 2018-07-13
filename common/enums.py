from enum import Enum


class clue_status_enum(Enum):
    '''
    线索状态
    '''
    auditing = 0
    rec = 1
    call = 2
    visit = 3
    order = 4
    sub = 5
    sign = 6
    returned = 7


class clue_mode_enum(Enum):
    '''
    线索类型
    '''
    alls = 1
    hide = 2


class clue_belong_enum(Enum):
    '''
    线索归属
    '''
    share = 100
    life = 200
    sale = 300
    external = 400


if __name__ == '__main__':
    print(clue_mode_enum.all.value)
