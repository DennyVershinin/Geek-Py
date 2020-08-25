time_sec = int(input("Введите время в секундах\n"))
hh = time_sec // 3600
rest = time_sec % 3600
mm = rest // 60
ss = rest % 60

print('введеное время:{}:{}:{}'.format(hh,mm,ss))