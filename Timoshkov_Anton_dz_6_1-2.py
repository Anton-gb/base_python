import json

with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
    p = json.load(f)

line = p.strip().split('\n')

box = []
spam = []

for i in line:
    _ip = i.split('-')
    ip = _ip[0].strip()
    spam.append(ip)
    _get = i.split('"')
    u = _get[1].split(' ')
    result = (ip, u[0], u[1])
    box.append(result)

print(box)

spam_dict = {}

for i in spam:
    spam_dict[i] = spam_dict.get(i, 0) + 1

print(f'Спамер: {max(spam_dict, key=spam_dict.get)}')
