n = int(input("Введите целое число больше 0\n"))
if n < 0:
    print("Число должно быть больше нуля!")
    exit(10)
i = 0
n = str(n)
num = 0
maximum = 0
while True:
    if i == len(n):
        break

    if int(n[i]) > int(maximum):
        maximum = n[i]
    num = n[i]
    i += 1
print("Наибольшая цифра в введенном числе:", maximum)
