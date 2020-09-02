def num_degree(a, b):
    i = 1
    a = 1 / a
    b = abs(b)
    res = a
    while i < b:
        res = res * a
        i += 1
    return res


x = float(input('Введите дейсвительное, положительное число х: '))
y = int(input('Введите целое отрицательно число у: '))

while True:
    if x <= 0:
        print('Число х должно быть больше 0')
        x = float(input('Введите дейсвительное, положительное число х: '))
    elif y >= 0:
        print('Число у должно быть отрицательным')
        y = int(input('Введите целое отрицательно число у: '))
    else:
        print(f'{x}^({y})={num_degree(x, y)}')
        break

