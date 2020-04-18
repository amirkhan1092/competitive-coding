# lazy bartender
from functools import reduce
import itertools

dct = eval(input())
valu = list(dct.values())  # val = [[0, 1, 3, 6], [1, 4, 7], [2, 4, 7, 5], [3, 2, 5], [5, 8]]
re = reduce(lambda x1, x2: set(x1) | set(x2), valu)
# main content

# { 0: [0, 1, 3, 6], 1: [1, 4, 7], 2: [2, 4, 7, 5], 3: [3, 2, 5], 4: [5, 8]}
l = []
for i, j in dct.items():
    for k in j:
        if (k not in l):
            l.append(k)
br = []
for i in range(1, len(l) + 1):
    br.extend(set(itertools.combinations(l, i)))
print(br)


for i in br:
     l2 = []
     for j in i:
         for k in dct.keys():
             if (j in dct[k]):
                 if (j in l):
                     l2.append(k)
             if (sorted(l2) == sorted(list(dct.keys()))):
                 print(len(i))
                 exit()




