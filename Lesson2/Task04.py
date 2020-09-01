str1 = str(input("введите строку: "))

str1 = str1.split()

i = 1
for st in str1:
    if len(st) > 10:
        print(i, "", st[0:10])
    else:
        print(i, "", st)
    i += 1
