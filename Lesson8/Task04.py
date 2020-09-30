class Stock:

    @staticmethod
    def recieve(types, quantity, model, color, tray_capacity=0, multipage=False, category=''):
        equipment = []

        pq = 0
        for x in range(quantity):
            if types == 'printer':
                item = str((Printer(types, 1, model, color, tray_capacity)))
                equipment.append(item)
            elif types == 'scanner':
                item = str((Scanner(types, 1, model, color, multipage)))
                equipment.append(item)
            elif types == 'xerox':
                item = str((Xerox(types, 1, model, color, category)))
                equipment.append(item)

        return equipment


class OfficeEquipment():
    types: str
    quantity: int
    model: str
    color: bool


class Printer(OfficeEquipment):
    tray_capacity: int

    def __init__(self, types: str, quantity: int, model: str, color: bool, tray_capacity):
        self.types = types
        self.quantity = quantity
        self.model = model
        self.color = color
        self.tray_capacity = tray_capacity

    def __str__(self):
        return f'тип:{self.types}, кол-во:{self.quantity}, модель:{self.model}, цветной:{self.color}, вместимость лотка:{self.tray_capacity}'


class Scanner(OfficeEquipment):
    multipage: bool

    def __init__(self, types: str, quantity: int, model: str, color: bool, multipage: bool):
        self.types = types
        self.quantity = quantity
        self.model = model
        self.color = color
        self.multipage = multipage

    def __str__(self):
        return f'тип:{self.types}, кол-во:{self.quantity}, модель:{self.model}, цветной:{self.color}, Многостраничный:{self.multipage}'


class Xerox(OfficeEquipment):
    category: str

    def __init__(self, types: str, quantity: int, model: str, color: bool, category):
        self.types = types
        self.quantity = quantity
        self.model = model
        self.color = color
        self.category = category

    def __str__(self):
        return f'тип:{self.types}, кол-во:{self.quantity}, модель:{self.model}, цветной:{self.color}, Тип:{self.category}'


a = Stock.recieve('printer', 3, 'HP', True, tray_capacity=100)
b = Stock.recieve('scanner', 2, 'Epson', False, multipage=True)
d = Stock.recieve('xerox', 4, 'Xerox', True, category='SOHO')

print(a)
print(b)
print(d)
