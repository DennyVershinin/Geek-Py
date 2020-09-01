product_template = {
    'название': ("имя товара", str),
    'цена': ('стоимость товара', int),
    'количество': ('количество товара', int),
    'ед': ('Единицы измерения (шт, кг, и тд)', str),
}

next_enter = True

increment = 1
product_list = []

while next_enter:
    product = {}

    for key, value in product_template.items():
        while True:
            user_value = input(f'{value[0]}\n')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f"{e}\nНе верное значение")
                continue
            product[key] = user_value
            break
    product_list.append((increment, product))
    increment += 1

    while True:
        next_add = input("Добавить продукт? Да/Нет\n")
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'да'
            break
        else:
            print('Неверный ввод, попробуйте еще раз')

print(product_list)

products_analytics = {}

for key in product_template:
    result = []
    for itm in product_list:
        result.append(itm[1][key])
    products_analytics[key] = result


print(products_analytics)