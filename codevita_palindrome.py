

n1, n2 = map(int,input().split())
patt = set()
s1 = ""
s2 = ""
s3 = ""
s4 = ""
s = ""
count = 0
l = []
for i in range(n1, n2+1):
    for j in range(0, 24):
        for k in range(0, 60):
            for o in range(0,60):
                s1 = str(i)
                if (j < 10):
                    s2 = "0" + str(j)
                else:
                    s2 = str(j)
                if (k < 10):
                    s3 = "0" + str(k)
                else:
                    s3 = str(k)
                if (o < 10):
                    s4 = "0" + str(o)
                else:
                    s4 = str(o)
                s = s1 + s2 + s3 + s4
                patt.add(s)
                l.append(s)
# checking initial and final value
print(min(l))
print(max(l))

#counting no of palindrome
for i in patt:
    if(i[::-1] in patt):
        count = count + 1
print(count//2)