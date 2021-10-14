import time


class TrafficLight:
    __color = [('красный', 7), ('жёлтый', 5), ('зелёный', 1)]

    def running(self):
        for i in TrafficLight.__color:
            print(i[0])
            time.sleep(i[1])


TrafficLight().running()

