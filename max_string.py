'''
input
1
xxaxaxax

output
xxxaxax

after removing k=1

'''

k = int(input())
st = input()

for i in sorted(st)[:k]:
    slt = list(st)
    slt.remove(i)
    st = ''.join(slt)
print(st)

