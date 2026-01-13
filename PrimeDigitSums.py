#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'primeDigitSums' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
mod = 1000000007
#nmax = 400000
def sieve(num):
    prime = [True]*num
    prime[0] = False
    prime[1] = False
    i = 2
    while i*i < num:
        x = i*i
        if prime[i]:
            q = 0
            while x+q < num:
                prime[x+q] = False
                q += i 
        i += 1
    res = set()
    for i in range(len(prime)):
        if prime[i]:
            res.add(i)
    return res
#parr = sieve(46)
parr = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43}
def psums(n):
    a = 0
    b = 0
    if n == 1:
        a = 1
        b = 10
    if n == 2:
        a = 10
        b = 100
    if n == 3:
        a = 100
        b = 1000
    res = 0
    for i in range(a, b):
        si = 0
        di = i
        ci = ''
        for j in range(n):
            li = di%10
            si += li
            ci = str(li)+ci
            di = di//10
        if si in parr:
            res += 1
    return res     
def primeDigitSums(n, dp):
    # Write your code here
    res = 0
    #dp[1] = psums(1)
    #dp[2] = psums(2)
    #dp[3] = psums(3)
    #print(parr)
    ps4 = defaultdict(int)
    for i in range(10000):
        si = 0
        di = i
        ci = ''
        sa = 0
        sb = 0
        for j in range(4):
            li = di%10
            si += li
            ci = str(li)+ci
            di = di//10
            if j > 0:
                sb += li
            if j < 3:
                sa += li
        if si in parr and sa in parr and sb in parr :
            ps4[ci] += 1
    #print(ps3)      
    #print(len(ps3))
    ps4a = defaultdict(list)
    prev = defaultdict(int)
    for pi in ps4.keys():
        li = list(map(int, pi))
        si = sum(li)
        if pi[0] != '0':
            prev[pi] = ps4[pi]
        for j in range(10):
            pj = pi[1:]+str(j)
            if si-li[0]-li[1]+j in parr and si-li[0]+j in parr and si+j in parr:
                ps4a[pi].append(pj)
    #print(len(ps4a.keys()), ps4a.keys())
    #print(prev.keys())
    #print(sum(prev.values()))
    dp[4] = sum(prev.values())
    m = 5
    res = 0
    while m <= n:
        curr = defaultdict(int)
        for pi in prev.keys():
            for pj in ps4a[pi]:
                curr[pj] += prev[pi]
                curr[pj] %= mod
                dp[m] += prev[pi]
                dp[m] %= mod
        prev = curr
        #print(len(curr))
        m += 1
    #print(dp)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    
    narr = []
    nmax = 0
    for q_itr in range(q):
        n = int(input().strip())
        narr.append(n)
        if n > nmax:
            nmax = n
    dp = [0]*(nmax+1)
    dp[0:4] = [0, 9, 90, 303]
    #print(parr)
    primeDigitSums(nmax, dp)
    for q_itr in range(q):
        result = dp[narr[q_itr]]
        fptr.write(str(result) + '\n')

    fptr.close()
