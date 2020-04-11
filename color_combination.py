

k = eval(input("enter the list of colors ")) # ["R", "G", "B", "R", "G", "R"]
st = {'R', 'G', 'B'}
i = 0
lst = []
print(k)
while len(k)> 1:
    if len(k) >= 2:
        while 1:
            s = set([k[i], k[i+1]])
            if len(s) > 1:
                print(s, end = '---> ')
                l = st - set((k.pop(i), k.pop(i)))
                k.insert(i, *l)
                print(l, end='\t')
                print(k)
                break
            else:
                i += 1
        i = 0
print(f'\nOutput is "{k}"')

