income = int(input("Введите выручку фирмы\n"))
costs = int(input("Введите сумму издержек фирмы\n"))

if income == costs:
    print("Выручка только покрывает убытки")
elif income > costs:
    print("Фирма имеет прибыль")
    clear_income = income - costs
    ren = int((clear_income / income) * 100)
    print("Чистая прибыль фирмы составляет:", clear_income,"рентабельность выручки составляет:", ren,"%")
    employees = int(input("Введите кол-во сотрудников фирмы:\n"))
    clear_income_per_employee = clear_income / employees
    print("Чистая прибыль на одного сотрудника составляет:", clear_income_per_employee,"\n")
else:
    print("фирма работает в убыток")
