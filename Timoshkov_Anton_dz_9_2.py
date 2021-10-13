class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        res = int(self._length * self._width * 25 * 5 / 1000)
        return res


a = Road(20, 5000)
print(a.weight())
