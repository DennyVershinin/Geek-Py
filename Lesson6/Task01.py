import time


class TrafficLight:
    __color: list = ['красный', 'желтый', 'зеленый']

    def running(self):
        for i in range(len(self.__color)):
            if  i==0:
                if self.__color[i] != 'красный':
                    print('нарушен порядок цветов!')
                    return 10
                print(self.__color[i])
                time.sleep(7)
            if i == 1:
                if self.__color[i] != 'желтый':
                    print('нарушен порядок цветов!')
                    return 10
                print(self.__color[i])
                time.sleep(2)
            if i == 2:
                if self.__color[i] != 'зеленый':
                    print('нарушен порядок цветов!')
                    return 10
                print(self.__color[i])
                time.sleep(3)




t = TrafficLight()

t.running()






