k = input()

if len(k) % 2 == 0:
    p = 0
    st = ''
    for i in range(len(k) // 2):
        st += k[p:p + 2][::-1]
        p += 2
    print(st)



else:
    print('Odd length.')