from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def cloth(self):
        return ""


class Coat(Parent):
    def __init__(self, size):
        self.size = size

    def cloth(self):
        print(self.size / 6.5 + 0.5)


class Costume(Parent):
    def __init__(self, height):
        self.height = height

    def cloth(self):
        print(2 * self.height + 0.3)


# Класс контейнер
class Wear:
    def __init__(self, *args):
        self.clothes = args

    def cloth(self):
        for i in self.clothes:
            # Вызываем метод класса, который передали в класс контейнер
            i.cloth()

    @property
    def my_method(self):
        return f"{self.clothes}"


a = Coat(44)
b = Costume(180)
wears = Wear(a, b)

# Проверка декоратора @property
wears.cloth()
print(wears.my_method)

