class Worker:
    name: str
    surname: str
    position: str
    _income: dict = {"wage": float, "bonus": float}


class Position(Worker):

    def get_full_name(self, name, surname):
        self.name = name
        self.surname = surname
        print(f'полное имя: {self.name} {self.surname}')

    def get_total_income(self, wage: int, bonus: int):
        self._income = {"wage": wage, "bonus": bonus}
        income = self._income.get("wage") + self._income.get("bonus")
        print('доход:', income)


p = Position()
t = Position()

p.get_full_name('John', 'Di')
p.get_total_income(100, 200)
t.get_full_name('Bryan', 'O\'conner')
t.get_total_income(150, 300)


