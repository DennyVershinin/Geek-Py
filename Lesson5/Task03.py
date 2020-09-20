s = 0
sum = 0
with open("task3.txt") as employees:
    for employee in employees:
        employee = employee.split(" ")
        if float(employee[1]) < 20000:
            print(f'{employee[0]} оклад:{employee[1]}')
            sum = sum + float(employee[1])
            s = s + 1
print(f'средняя ЗПшка отдела разработчиков: {sum /s}')