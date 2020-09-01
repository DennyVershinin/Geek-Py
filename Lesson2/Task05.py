my_list = [7, 5, 3, 3, 2]

print("рейтинг: ", my_list, "\n")
el = int(input("введите новый элемент рейтинга (целое число) : "))

for l in range(len(my_list) - 1):
    if el > my_list[0]:
        my_list.insert(l, el)
        break
    elif my_list[l] >= el and el >= my_list[l + 1]:
        my_list.insert(l+1, el)
        break
    elif el < my_list[len(my_list)-1]:
        my_list.insert(len(my_list), el)
        break

print(f"новый рейтинг: {my_list}")
