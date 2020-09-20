numbers = open("Task4.txt", "w")
n = input('введите числа для подсчета их суммы через пробел ')
numbers.write(n)
numbers.close()

res = 0
numbers = open("Task4.txt", "r")
n = numbers.read()
n = n.split(' ')
print(len(n))
for i in n:
    res = res + int(i)
print(res)
numbers.close()



