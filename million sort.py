import math

n = int(input().strip())
lst = input()
comb = 1
pt = 0
for i in range(1, n+1):
    comb *= i
    pt += 1/i

groups = math.ceil(comb*pt)
out = groups/comb
print('{0:.6f}'.format(out))
