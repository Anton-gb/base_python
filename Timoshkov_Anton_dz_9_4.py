class Car:
    def __init__(self, speed, color, name, is_police=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = None

    @staticmethod
    def go():
        print('Машина поехала')

    @staticmethod
    def stop():
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f"Машина повернула {self.direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на {self.speed - 60}")
        else:
            print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости на {self.speed - 60}")
        else:
            print(f"Скорость - {self.speed}")


class PoliceCar(Car):
    pass


a = SportCar(100, 'yellow', 'F')
print(a.name)
a.show_speed()
a.turn('направо')

b = TownCar(70, 'yellow', 'W')
print(b.name)
b.show_speed()

c = WorkCar(40, 'yellow', 'L')
print(c.name)
c.go()
c.show_speed()
