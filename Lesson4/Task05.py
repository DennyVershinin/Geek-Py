from functools import reduce

def multiplier(el_prev, el):
    return el_prev * el

res = [x for x in range(100,1002) if x % 2 == 0]
print(res,"\n")

print(reduce(multiplier, res, 100))