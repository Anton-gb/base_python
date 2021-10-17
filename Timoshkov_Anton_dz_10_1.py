class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        # Определяем атрибуты для дальнейшего использования
        self.__new_matrix = None
        self.__box = None

    def __str__(self):
        for i in self.matrix:
            print(f"{i}")
        return ""

    def __add__(self, other):
        # Контейнер для новой матрицы
        self.__new_matrix = []
        # Перебираем строки в матрицах
        for i, j in zip(self.matrix, other.matrix):
            # Контейнер для строки матрицы
            self.__box = []
            # Проверка, что матрицы одинакового размера
            if len(i) == len(j):
                for indx, val in enumerate(i):
                    self.__box.append(val + j[indx])
                self.__new_matrix.append(self.__box)
            else:
                self.__new_matrix = None
                return self.__new_matrix
        # Передаем новую матрицу в класс Matrix
        return Matrix(self.__new_matrix)


a = Matrix([[31, 22], [37, 43], [51, 86]])
print(a)

b = Matrix([[4, -2], [6, 9], [51, -10]])
print(b)

c = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(c)

d = a + b
print(d)

f = a + c
print(f)

