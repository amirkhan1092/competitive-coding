'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

import random
import itertools
N = int(input())  # number of steps
climb = eval(input())  # set of climbs steps taken by user example climb = [1, 2]
# print(list(itertools.combinations(climb, N)))

k = [[i]*N for i in climb]
pk = [i for p in k for i in p]
L = []
for i in range(1, N+1):
    for comb in itertools.combinations(pk, i):
        if sum(comb) == N:
            L.append(comb)

print(set(L))



