class ZeroDivisionCheck(Exception):
    def __init__(self, devident: float, devider: float):
        self.devident = devident
        self.devider = devider

    def __str__(self):
        return f'ZeroDivision is depricated!'



a = float(input('введите делимое'))
b = float(input('введите делитель'))


try:
    if b == 0:
        raise ZeroDivisionCheck(a, b)
except ZeroDivisionCheck as exception:
    print(f'Devider is {exception.devider}!!')
else: print(f'a / b = {a / b}')

