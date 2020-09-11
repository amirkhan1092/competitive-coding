# This problem was asked by Google.
# You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string.
# Determine whether the parentheses are balanced.
# For example, (()* and (*) are balanced. )*( is not balanced.
st = input()
count = 0
for c, i in enumerate(st):
    if i == '(':
        count += 1
    elif i == ')':
        count -= 1
        if count < 0 and '*' not in st[:c+1]:
            print(False)
            break
        elif count < 0 and '*' in st[:c+1]:
            count += 1
    elif i == '*':
        if count >= 1:
            count -= 1
        else:
            count += 1
else:
    print(True if not count else False)
