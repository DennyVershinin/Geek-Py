def summarise(numbers):
    sum_n = 0
    for number in numbers:
        if number == 'q':
            return sum_n, 'q'
        try:
            number = 0 + float(number)
        except ValueError as number:
            print(f"{number} - Не верное значение")
            continue
        sum_n = sum_n + float(number)
    return sum_n, 'y'


n = str(input('введите строку чисел, разделенных пробелом'))
n = n.split()


stop = 'y'
result = 0
while True:
    sum, stop = summarise(n)
    result = result + sum
    print('Сумма введенных чисел = ', result, '\n')
    if stop == 'q':
        break
    n = str(input('Если хотите добавить чисел к сумме, введите их черех пробел. Для выхода введите q: '))
    n = n.split()

