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

lt = sorted(st)
for i in range(k):
    slt = list(st)
    slt.remove(lt[i])
    st = ''.join(slt)
print(st)

