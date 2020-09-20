res = open("Task3_2_result.txt", "w")

with open("Task3_2.txt") as numbers:
    for number in numbers:
        if number.find('One') == 0:
            res.write('Один - 1\n')
        if number.find('Two') == 0:
            res.write('Два - 2\n')
        if number.find('Three') == 0:
            res.write('Три - 3\n')
        if number.find('Four') == 0:
            res.write('Четыре - 4\n')

res.close()