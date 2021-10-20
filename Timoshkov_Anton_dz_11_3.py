class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


box = []
inp_num = None
while inp_num != 'stop':
    print('Введите stop если хотите закончить')
    inp_num = input('Введите число: ')
    try:
        if inp_num.isdigit():
            inp_num = int(inp_num)
            box.append(inp_num)
        else:
            raise OwnError('Введите число!!!')
    except OwnError as err:
        print(err)
else:
    print('Введение числа')
    print(box)

