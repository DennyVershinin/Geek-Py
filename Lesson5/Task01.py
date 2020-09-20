print('Введите текст для записи в файл. Для завершения ввода нажмите Enter 2 раза\n')

text = []
while True:
    t = input()
    text.append(t)
    if t == "":
        break

formatted_text = [f'{line}\n' for line in text]
my_f = open("task1.txt", 'w')
for t in formatted_text:
    my_f.write(t)
my_f.close()
