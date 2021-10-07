class Stationery:
    def __init__(self, title=None):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    @staticmethod
    def draw():
        print('Отрисовка ручкой')


class Pencil(Stationery):
    @staticmethod
    def draw():
        print('Отрисовка карандашом')


class Handle(Stationery):
    @staticmethod
    def draw():
        print('Отрисовка маркером')


Stationery().draw()
Pen().draw()
Pencil().draw()
Handle().draw()
