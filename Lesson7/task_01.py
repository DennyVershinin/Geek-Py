class Matrix:
    def __init__(self, *args):
        self.new_lst = []
        for elem in args:
            self.new_lst.append(elem)

    def __str__(self):
        result = '\n'.join(map(str, self.new_lst))
        result = result.replace(',', '').replace('[', '').replace(']', '')
        return result

    def __add__(self, other):
        new_sum = []
        line_sum = []
        for x in range(len(self.new_lst)):
            for y in range(len(self.new_lst[x])):
                # создаем список сумм элементов каждой строки
                line_sum.append(self.new_lst[x][y] + other.new_lst[x][y])
            # вносим каждую строку в виде списка в результируюший список
            new_sum.append(line_sum)
            # обнуляем список для внесения сум элементов следующей строки
            line_sum = []
        return Matrix('\n'.join(map(str, new_sum)))


M_OBJ_1 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_OBJ_1)
print()

M_OBJ_2 = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(M_OBJ_2)
print()

print(f'Сумма матриц:\n{M_OBJ_1 + M_OBJ_2}')
