#
# Harry to Hogwarts

num = input('enter the digits ')
kh = ''.join(sorted(num))
tm = '6174'
count = 0
while tm != kh:
    kh = str(int(''.join(sorted(kh, reverse=True))) - int(''.join(sorted(kh))))
    count += 1

print(count)
