# lazy bartender
from functools import reduce
from itertools import combinations

dct = eval(input())
valu = list(dct.values())  # val = [[0, 1, 3, 6], [1, 4, 7], [2, 4, 7, 5], [3, 2, 5], [5, 8]]
l = list(reduce(lambda x1, x2: set(x1) | set(x2), valu))
# main content

# { 0: [0, 1, 3, 6], 1: [1, 4, 7], 2: [2, 4, 7, 5], 3: [3, 2, 5], 4: [5, 8]}

all_combination = []  # [(0,) (0, 1)]
for i in range(1, len(l) + 1):all_combination.extend(set(combinations(l, i)))
# print(all_combination)

for i in all_combination:  # iterate to find the perfect combination
    tt = []
    for j in i:
        for k in dct.keys():
            if (j in dct[k]):
                tt.append(k)
    if set(tt).issuperset(dct.keys()):  # check the combination satisfying the all keys
        print(i)  # items common
        print(len(i))  # length of items (needed in example )
        break




