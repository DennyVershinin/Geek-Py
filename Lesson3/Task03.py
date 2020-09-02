def my_func(num1, num2, num3):
    if num1 > num2:
        if num2 > num3:
            return num1 + num2
        else:
            return num1 + num3
    else:
        return num2 + num3


# a, b, c = input('введи ка 3 числа: ')
nums = input('введите 3 числа, разделенных запятой')
a, b, c = nums.split(',')
a, b, c = int(a), int(b), int(c)
print(f'сумма двух наибольших чисел = {my_func(a, b, c)}')