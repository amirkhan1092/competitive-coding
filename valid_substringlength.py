s = input()
l = 0
r = 0
x = 0
pos = 0
flag = 0
s1 = ""
if len(s) < 2:
    print("0")
else:
    for i in range(len(s)):
        if s[i] == "(":
            x += 1
            l += 1
            if(flag == 0):
                pos = i
            flag = 1
        elif s[i] == ")" and flag == 1:
            x -= 1
            r += 1
        if x == 0 and flag == 1:
            s1 = s1 + s[pos:i+1]
            pos = i+1
            flag = 0
    if s1 == "" and x > 0:
        c = len(s) - (l - r)
        print(c)
    else:
        print(len(s1))