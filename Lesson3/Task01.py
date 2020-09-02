def del_func(num1, num2):
    return num1 / num2


a = int(input('введите число а '))
b = int(input('введите число b (равное 0) '))
while True:
    if b == 0:
        b = int(input("b = 0! введите еще раз число b "))
    else:
        break
print('a / b = ', del_func(a, b))
