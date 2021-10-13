import time


class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        for i in TrafficLight.__color:
            print(i)
            if i == 'красный':
                time.sleep(7)
            elif i == 'жёлтый':
                time.sleep(5)
            else:
                time.sleep(1)


TrafficLight().running()

