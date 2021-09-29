import sys

price = sys.argv[1]
# price = '2,2'

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(price + '\n')

# with open('bakery.csv', 'w', encoding='utf-8') as f:
#     pass

