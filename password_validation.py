# validation char Alphabet(Upper and Lower), Digit(0-9), Special Char and len > 8
st = input()  # enter the password
d = au = al = sc = 0
if len(st) >= 8:
    for i in st:
        if i.isdigit():
            d += 1
        elif i.isupper():
            au += 1
        elif i.islower():
            al += 1
        else:
            sc += 1
if all([d, au, al, sc]):
    print('valid password you set ')
else:
    print('not a valid password you set : ')

h = f'''
Digits: {d}
Upper Alphabet: {au}
Lower Alphabet: {al}
Special Char: {sc} 
'''
print(h)


# get valid password from user forcely
pas = ' '
while pas:
    pas = input('enter the valid password Min 1Upper/1Lower/1Digit/1Special and len>8 ')
    if len(pas) > 8:
        pass


