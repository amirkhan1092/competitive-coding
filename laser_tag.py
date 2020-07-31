# import itertools as ite

team, hr = map(int, input().split())

if (team-1)*30/60 <= hr:
    print(1)
else:
    print(0)
