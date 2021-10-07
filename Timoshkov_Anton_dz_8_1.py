import re

RE_DATE = re.compile(r'^(\d{2}\.){2}\d{4}$')

for date in ['23.01.2021', '23,01,2021', '23~01~2021']:
    print(RE_DATE.match(date), f'wrong date {date}')
