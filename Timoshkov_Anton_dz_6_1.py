import requests
import json

text = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

line = text.text.strip().split('\n')

# test = '''93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 93.180.71.3 - - [17/May/2015:08:05:23 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
# 80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
# 80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"
# '''

box = []
spam = []

# line = test.strip().split('\n')

for i in line:
    _ip = i.split('-')
    ip = _ip[0].strip()
    spam.append(ip)
    _get = i.split('"')
    u = _get[1].split(' ')
    result = (ip, u[0], u[1])
    box.append(result)

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    json.dump(box, f)
    

# gg = {}
#
# for i in spam:
#     gg.setdefault(i, len(list(filter(lambda x: x == i, spam))))
#
# print(max(gg, key=gg.get))
