for i in range(1, 101):
    if i == 11:
        print(f'{i} процентов')
    elif i % 10 == 1:
        print(f'{i} процент')
    elif 1 < i % 10 < 5:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')
