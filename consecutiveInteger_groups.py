for _ in range(int(input())):
    p = int(input())
    lst = []
    ls = list(map(int, input().strip().split()))
    tmpl = []


    for i in range(len(ls)-1):
        if ls[i+1] - ls[i] == 1:
            tmpl.append(ls[i])
            if i == len(ls)-2:
                tmpl.append(ls[i+1])
                lst.append(tmpl)

        else:
            tmpl.append(ls[i])
            lst.append(tmpl)
            tmpl = []
    print(lst)
    print(len(list(filter(lambda x:len(x)>1, lst))))