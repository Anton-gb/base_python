price = [57.8, 46.51, 97, 10.01, 8.09, 1.1, 101.4, 88.88, 90, 60.03]
print(id(price))

for i in price:
    rub = int(i)
    penny = (i - rub) * 100
    penny = f"{penny:.0f}"
    print(f"{rub} руб {penny:0>2} коп", end=', ')
print('')
# цены по возрастанию
print('ЦЕНЫ ПО ВОЗРАСТАНИЮ: ')
price.sort()
print(price)
print(id(price))
# цены по убыванию
print('ЦЕНЫ ПО УБЫВАНИЮ: ')
price.reverse()
print(price)
print(id(price))
# топ 5
print('ТОП 5: ')
print(price[:5])
# топ 5 (2)
for _, i in enumerate(price[:5], 1):
    print(_, i)
