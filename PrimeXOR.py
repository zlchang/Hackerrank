#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'primeXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def primeXor(a):
    # Write your code here
    mod = 1000000007
    nmax = (1<<13)
    #print(nmax)
    prime = [True]*nmax
    prime[0] = False
    prime[1] = False
    i = 2
    while i*i < nmax:
        if prime[i]:
            x = i*i
            while x < nmax:
                prime[x] = False
                x += i
        i += 1

    counter = defaultdict(int)
    
    for x in a:
        counter[x] += 1
    nx = len(counter.keys())
    key = list(counter.keys())
    arr = [[0 for i in range(nmax)] for j in range(nx+1)]
    arr[0][0] = 1
    for i in range(1, nx+1):
        ki = key[i-1]
        nk = counter[ki]
        for j in range(nmax):
            xor = ki^j
            arr[i][j] = arr[i-1][j]*(nk//2+1) + arr[i-1][xor]*((nk+1)//2)
            arr[i][j] %= mod
    res = 0
    for i in range(nmax):
        if prime[i]:
            #print(i, arr[nx][i])
            res += arr[nx][i]
            res %= mod
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = primeXor(a)

        fptr.write(str(result) + '\n')

    fptr.close()
