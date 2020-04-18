# lazy bartender
from functools import reduce
h = eval(input())
valu = list(h.values())

re = reduce(lambda x1, x2: x1 | x2, valu)

print(re)