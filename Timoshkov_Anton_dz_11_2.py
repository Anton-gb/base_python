class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_denominator = int(input("Введите число, на которое хотите разделить: "))
inp_numerator = int(input("Введите число, которое хотите разделить: "))

try:
    if inp_denominator == 0:
        raise OwnError('На ноль делить нельзя!!!')
except OwnError as err:
    print(err)
else:
    result = inp_numerator / inp_denominator
    print(result)
