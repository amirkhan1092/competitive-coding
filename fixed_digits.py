import time

num = input('enter the digits ')
kh = ''.join(sorted(num))
tm = '6174'
count = 0
while tm != kh:
    kh = str(int(''.join(sorted(kh, reverse=True))) - int(''.join(sorted(kh))))
    count += 1

print(count)

h = 'R\x1e\x00\x00\x00\x00\x00\x00\n\xcf<\n\xf0\x02\n\x08abstract\x12\xe3\x02\n\xe0\x02\n\xdd\x02<s> marseille prosecutor says'
print(h)