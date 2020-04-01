
# This problem was asked by Quora.
# You are given a list of (website, user) pairs that represent users visiting websites. Come up with a program that identifies the top k pairs of websites with the greatest similarity.
# For example, suppose k = 1, and the list of tuples is:
# [('a', 1), ('a', 3), ('a', 5),  ('b', 2), ('b', 6),  ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)  ('d', 4), ('d', 5), ('d', 6), ('d', 7),  ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
# Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].

from itertools import combinations
data = eval(input())  # enter the data list web user pair
cmp = int(input())  # enter number of pairs k = 1

match = None
d = {}
for i, j in data:
    if i == match:
        d[i].append(j)
    else:
        d[i] = [j]
        match = i
res = []
for y, k in combinations(d.keys(), 2):
    res.append(([y, k], len(set(d[y]) ^ set(d[k]))))

# print(res)
p = min(res, key=lambda x:x[1])
for i in range(cmp):
    print(p[i])


# [('a', 1), ('a', 3), ('a', 5),  ('b', 2), ('b', 6),  ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5) , ('d', 4), ('d', 5), ('d', 6), ('d', 7),  ('e', 1), ('e', 3), ('e', 5), ('e', 6)]