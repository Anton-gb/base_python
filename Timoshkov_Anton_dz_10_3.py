class Cell:
    def __init__(self, num):
        self.num = num
        self.result = None
        self.cells = None

    def __add__(self, other):
        self.result = self.num + other.num
        return Cell.make_order(self.result)

    def __sub__(self, other):
        self.result = abs(self.num - other.num)
        if self.result > 0:
            return Cell.make_order(self.result)
        else:
            return f"no"

    def __mul__(self, other):
        self.result = self.num * other.num
        return Cell.make_order(self.result)

    def __truediv__(self, other):
        self.result = int(self.num / other.num)
        return Cell.make_order(self.result)

    @staticmethod
    def make_order(cells):
        s = ''
        for i in range(cells):
            s += '*'
            if s.count('*') % 5 == 0:
                s += '\n'
        return s


a = Cell(3)
b = Cell(4)
print('Сложение')
res = a + b
print(res)
print('Вычитание')
res = a - b
print(res)
print('Умножение')
res = a * b
print(res)
print('Деление')
res = a / b
print(res)

