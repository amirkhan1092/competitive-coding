'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Epic.

The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
'''
import itertools as itr
N = int(input())
S = input()  # sequence starts here S = 1
print(S)
for i in range(N-1):
    for key, td in itr.groupby(S):
        S = key+str(len(list(td)))
        print(S, end='')
    print()
