lines = 0
words = 0
with open("Task2.txt") as poem:
    for line in poem:
        lines = lines + 1
        line = line.split(" ")
        for word in line:
            words = words + 1
        print(f'строка {lines} кол-во слов: {words}')
        words = 0

print(f'всего строк:{lines}')