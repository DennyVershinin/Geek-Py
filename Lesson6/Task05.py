class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Ручка пишет')

class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')

class Handle(Stationery):
    def draw(self):
        print('Маркер рисует')


stationery = Stationery('unknown')
pen = Pen('ручка')
pencil =Pencil ('карандаш')
handle = Handle('Маркер')

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()



