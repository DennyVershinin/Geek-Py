from sys import argv


def salary(hours, rate, bounty):
    return int((hours * rate) + bounty)


try:
    file, w_hours, h_rate, b_bounty = argv
except ValueError:
    print("Введите аргументы через пробел - кол-во отработанных часов, ставку, премию")
    exit()

print(w_hours, h_rate, b_bounty)
s = salary(int(w_hours), int(h_rate), int(b_bounty))

print(f"Зарплата за отработанные часы + премия : {s}")
