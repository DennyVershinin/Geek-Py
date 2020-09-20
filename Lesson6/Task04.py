class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police = bool):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'Машина {self.name}, цвета {self.color} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')


class TownCar(Car):
    is_police = False


    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    is_police = False

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name


class WorkCar(Car):
    is_police = False

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    is_police = True

    def go(self):
        print(f'Полицейская машина {self.name}, цвета {self.color} поехала')


batmobile = Car(300, 'black', 'batmobile')
car_1 = TownCar(30, 'вишневый', '2109')
car_2 = SportCar(200, 'серый', '911')
car_3 = WorkCar(70, 'черный', 'волга')
police_car = PoliceCar(140, 'белый', 'ford')


batmobile.go()
batmobile.show_speed()
batmobile.turn('Направо')
batmobile.stop()



car_1.go()
car_1.show_speed()
car_1.turn('налево')
car_1.stop()
car_1 = TownCar(66, 'вишневый', '2109')
car_1.go()
car_1.show_speed()



car_2.go()
car_2.show_speed()
car_2.turn('направо')
car_2.turn('налево')
car_2.stop()


car_3.go()
car_3.show_speed()
car_3.turn('направо')
car_3.turn('налево')
car_3.stop()

police_car.go()
police_car.show_speed()
police_car.turn('направо')
police_car.turn('налево')
police_car.stop()


