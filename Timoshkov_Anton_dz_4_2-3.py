import requests
import datetime


def currency_rates(name):
    text_xml = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if text_xml.text.find(name.upper()) >= 0:
        # получения курса валюты
        value_name = text_xml.text.find(name.upper())
        _find_va = text_xml.text.find('</Va', value_name)
        _text = text_xml.text[value_name:_find_va]
        g = _text.split('<Value>')
        value = g[-1]
        if ',' in value:
            value = float(value.replace(',', '.'))
        # получение даты
        _find_date = text_xml.text.find('Date')
        _find_name = text_xml.text.find("name")
        _z = text_xml.text[_find_date:_find_name].split('"')
        _date = _z[1].split('.')
        date = datetime.date(int(_date[-1]), int(_date[1]), int(_date[0]))
        result = f"{value} {date}"
        return result
    else:
        return None


if __name__ == '__main__':
    print(currency_rates('EUR'))
    print(currency_rates('eUr'))
    print(currency_rates('Eng'))
