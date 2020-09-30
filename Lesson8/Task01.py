class Data:
    def __init__(self, data: str):
        self.data = data

    @classmethod
    def get_date(cls, data):
        date = data.split('-')
        day = (int(date[0]))
        month = (int(date[1]))
        year = (int(date[2]))
        print(f'typed date is:{day}-{month}-{year}')
        Data.valid_date(day, month, year)

    @staticmethod
    def valid_date(day: int, month: int, year: int):
        if day >= 1 and day <= 31:
            print(f'Day {day} is valid')
        else:
            print(f'Day {day} must be between 1 and 31')
        if month >= 1 and month <= 12:
            print(f'Month {month} is valid')
        else:
            print(f'Month {month} must be between 1 and 12')
        if year >= 1 and year <= 2020:
            print(f'Year {year} is valid\n ')
        else:
            print(f'Year {year} must be between 1 and 2020\n ')


Data.get_date('50-12-2021')
Data.get_date('31-06-2010')
