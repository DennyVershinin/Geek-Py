n = int(input("Введите необходимое кол-во элементов списка\n"))
myList = []

for k in range(n):
    new_item = (input())
    myList.append(new_item)


for i in range(n - 1):
    if i % 2 == 0:
        myList[i], myList[i + 1] = myList[i + 1], myList[i]
    else:
        continue

print("\nИзмененный список: ", myList)
