b = 'banana'
c = 'ana'
count = 0
for i in range(len(b) - len(c) + 1):
    if b[i:len(c) + i] == c:
        count += 1
print(count)
