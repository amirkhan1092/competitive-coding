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
# pas = ' '
dct = {'special char': 0, 'digits': 0, 'alpha lower': 0, 'alpha upper': 0}
while 1:
    pas = input('\n\nenter the valid password Min 1Upper/1Lower/1Digit/1Special and len>8 ')
    if len(pas) >= 8:
        for i in pas:
            if i.isdigit():
                dct['digits'] += 1
            elif i.isupper():
                dct['alpha upper'] += 1
            elif i.islower():
                dct['alpha lower'] += 1
            else:
                dct['special char'] += 1
        print('user entered ')
        print(f'''
        Digits: {dct['digits']}
        Upper Alphabet: {dct['alpha upper']}
        Lower Alphabet: {dct['alpha lower']}
        Special Char: {dct['special char']} 
        ''')
        if all(dct.values()):
            print('valid password ')
            print('welcome to the board ')
            break
        else:
            print('not a valid password ')
            print('user not entered', end=':--- ')
            for i in dct:
                if dct[i] == 0:
                    print(i, end=',')

    else:
        print('enter valid length again ')

