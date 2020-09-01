month = int(input("Введите номер месяца месяца:"))

list_year = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
             'декабрь']

dict_year = {
    'key_1': 'зима',
    'key_2': 'весна',
    'key_3': 'лето',
    'key_4': 'осень'
}

for i in range(len(list_year)):
    if i == month - 1:
        print(f"введенный месяц - {list_year[i]}")
        print(month)

if 1 <= month <= 2 or month == 12:
    print(f"Введенный месяц относится к периоду {dict_year.get('key_1')}")
elif 3 <= month <= 5:
    print(f"Введенный месяц относится к периоду {dict_year.get('key_2')}")
elif 6 <= month <= 8:
    print(f"Введенный месяц относится к периоду {dict_year.get('key_3')}")
elif 9 <= month <= 11:
    print(f"Введенный месяц относится к периоду {dict_year.get('key_4')}")
else:
    print("введенное число не является номером месяца")

