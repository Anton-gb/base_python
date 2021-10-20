class DateGet:
    date = None

    def __init__(self, date):
        DateGet.date = date

    @classmethod
    def parc_date(cls):
        list_date = cls.date.split('-')
        _list = ['число', 'месяц', 'год']
        _dict = {}
        indx = 0
        for i in _list:
            list_date[indx] = int(list_date[indx])
            if cls.valid_date(i, list_date[indx]):
                _dict[i] = list_date[indx]
            else:
                raise f'Неверный формат даты {list_date[indx]}'
            indx += 1
        return _dict

    @staticmethod
    def valid_date(param_1, param_2):
        _dict1 = {
            'число': 31,
            'месяц': 12,
            'год': None
        }
        if param_1 == 'год':
            return True
        elif param_2 <= _dict1.get(param_1):
            return True
        else:
            return False


a = DateGet('14-13-2018')
print(a.parc_date())
