class Cell:
    def __init__(self, num):
        self.num = num
        self.result = None

    def __add__(self, other):
        n = max(self.num, other.num)
        # Клетка без пары
        h = abs(self.num - other.num)
        # Количество пар
        self.result = n - h
        # Количество ячеек
        sum_cell = self.num + other.num

    def __sub__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __truediv__(self, other):
        pass


a = Cell(3)
b = Cell(4)

