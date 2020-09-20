class Road:
    _length: float
    _width: float

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self):
        meter_weight = input('введите массу асфальта, для покрытия одного кв метра дороги толщиной 1см ')
        sm = input('введите необходимую толщину полотна ')
        result = int(self._length) * int(self._width) * int(meter_weight) * int(sm)
        print(f'масса асфальта, необходимая для покрытия все дороги: {result} КГ')



l = input('введите длинну дороги ')
w = input('введите ширину дороги ')

my_road = Road(l,w)
my_road.weight()



