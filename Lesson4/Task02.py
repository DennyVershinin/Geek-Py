first_list = input('введите список чисел через пробел')
first_list = first_list.split()

result_list = [first_list[i] for i in range(1, len(first_list) - 1) if int(first_list[i - 1]) < int(first_list[i])]
print(result_list)
