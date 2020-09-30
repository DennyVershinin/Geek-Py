class ListNumbersCheck(Exception):
    def __init__(self, currnet):
        self.current = currnet

    def __str__(self):
            return f"Введено {self.current} - не число"


class CheckElement:
    @staticmethod
    def check(current):
        try:
            float(current)
        except:
            raise ListNumbersCheck(current)


my_list = []

while (True):
    a = (input('\n Введите элемент списка. Чтобы завершить ввод введите stop '))
    if a == 'stop':
        print(my_list)
        break
    try:
        CheckElement.check(a)
    except ListNumbersCheck as exception:
        print(f'{exception.current} - не является числом')
        continue
    my_list.append(a)
    print(my_list)
