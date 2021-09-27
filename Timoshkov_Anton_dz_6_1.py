import requests

text = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

line = text.text.strip().split('\n')

box = []
spam = []

for i in line:
    _ip = i.split('-')
    ip = _ip[0].strip()
    spam.append(ip)
    _get = i.split('"')
    f = _get[1].split(' ')
    result = (ip, f[0], f[1])
    box.append(result)

# for i in box:
#     print(i)

print(spam)
