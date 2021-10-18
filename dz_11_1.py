import re


class DateGet:
    date = None

    def __init__(self, date):
        DateGet.date = date

    @classmethod
    def parc_date(cls):
        list_date = cls.date.split('-')
        print(list_date)

    @staticmethod
    def valid_date(param_1):
        pass


def chek(data):
    While True:
        re_date = re.compile(r'^(\d{2}[./-]){2}\d{4}$')
        assert re_date.match(data)


# enter_data = input('Введите дату формата «день-месяц-год»')
a = DateGet('15-9-2018')
a.parc_date()


