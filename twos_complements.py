k = list(map(int, input().split()))

s = 0
for i in k:
    s += ~i
print('YES' if '0' in str(s) else 'NO')