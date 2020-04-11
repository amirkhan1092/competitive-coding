k = input()
l = 0
r = 0
u = 0
d = 0
for i in k:
    if i == 'U':
        u += 1
    elif i == 'D':
        d += 1
    elif i == 'R':
        r += 1
    elif i == 'L':
        l += 1

if l == r and u == d:
    print('true')
else:
    print('false')