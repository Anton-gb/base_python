name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

for i in name_list:
    n = i.split(' ')
    print(f"Привет, {n[-1].capitalize()}!")
