#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#
md = 1000000007
ff = []
mf = []
cntr = []
x = [0]
y = [0]
def gcd(a, b, x, y):
    if a == 0:
        x[0] = 0
        y[0] = 1
        return b
    
    r = gcd(b%a, a, x, y)
    x1 = x[0]
    y1 = y[0]
    x[0] = - (b//a) *x1 + y1
    y[0] = x1
    return r
        
def initialize(s):
    # This function is called once before all queries.
    global ff
    global mf
    global cntr 
    n = len(s)
    ff = [0]* (n+1)
    ff[0] = 1
    for i in range(1,n+1):
        ff[i] = (ff[i-1]*i)%md
    #print(ff)
    mf = [0]* (n+1)
    gcd(ff[n], md, x, y)
    mf[n] = (x[0]%md+md)%md
    #mf[n] = power(2, 6)
    for i in range(n, 0, -1):
        mf[i-1] = (mf[i]*i)%md
    #print(mf[n])
    cntr = [[0 for i in range(26)] for j in range(n+1)]
    for i in range(n):
        j = ord(s[i])-ord('a')
        for k in range(26):
            if k == j:
                cntr[i+1][j] = 1+cntr[i][j]
            else:
                cntr[i+1][k] = cntr[i][k]
    print(cntr)   
#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    sq = 0
    sm = 0
    ss = 1
    for i in range(26):
        v = cntr[r][i] - cntr[l-1][i]
        #if v == 0:
            #continue
        #print(i, v)
        q = v // 2
        sq += q
        m = v % 2
        sm += m
        ss = (ss*mf[q])%md
    rr = (ff[sq]*ss)%md
    if sm > 0:
        rr = (rr*sm)%md
    return rr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
