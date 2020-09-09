first_list = input('введите список чисел через пробел')
first_list = first_list.split()

res_list = []
res_list = [first_list[i] for i in range(0, len(first_list)) if first_list[i] not in [first_list[j] for j in range(0,len(first_list)) if i != j]]

print(res_list)
