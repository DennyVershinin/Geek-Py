class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def get_coat_consumption(self):
        return str(f'Расход ткани на пальто = {(self.v / 6.5 + 0.5):.2f}')

    def get_suit_consumption(self):
        return str(f'Расход ткани на костюм = {(self.h * 2 + 0.3):.2f}')

    @property
    def get_total_consumption(self):
        return str(f'Общий расход ткани = {((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)):.2f}')


class Coat(Clothes):
    def __init__(self):
        super().__init__()
        self.coat_consumption = round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто = {self.coat_consumption}'


class Suit(Clothes):
    def __init__(self):
        super().__init__()
        self.suit_consumption = round(self.h * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм = {self.suit_consumption}'


clothes = Clothes(5, 10)

print(clothes.get_total_consumption)
print(clothes.get_coat_consumption())
print(clothes.get_suit_consumption())
