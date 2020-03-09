# large fibonacci last digit number
num = int(input())  # enter the number
a, b = 0, 1
for i in range(num):a, b = b, a + b
print(str(b)[-1])