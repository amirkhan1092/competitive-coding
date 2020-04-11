def leap_year(y):
    return  y%4 == 0 and y%100 != 0 or y%400 == 0



k = int(input())
print(leap_year(k))
