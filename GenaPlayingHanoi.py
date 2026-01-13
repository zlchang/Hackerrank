#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hanoi' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY posts as parameter.
#

def hanoi(posts):
    # Write your code here
    m = 4
    n = len(posts)
    mstate = 1 << 2*n
    state = 0
    ff = 0
    estate = 0
    for i in range(n):
        pi = posts[i]-1
        state |= pi << ff
        ff += 2
    visited = [0]*mstate
    res = 0
    #print(state, estate)
    qq = []
    qq.append([state, res])
    visited[state] = 1
    head = 0
    tail = 1
    while head < tail:
        q, step = qq[head]
        head += 1
        if q == estate:
            return step
            
        tops = [-1]*m
    
        for i in range(n):
            pp = q >> 2*i  & 0x3
            if tops[pp] == -1:
                tops[pp] = i
    
        for i in range(m):
            ti = tops[i]
            if ti == -1:
                continue
            for j in range(m):
                tj = tops[j]
                if tj == -1 or ti < tj:
                    nstate = q - (i << 2*ti) + (j << 2*ti)
                    #print(nstate)
                    if visited[nstate] == 0:
                        qq.append([nstate, step+1])
                        visited[nstate] = 1
                        tail += 1
    return 0    
                 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    loc = list(map(int, input().rstrip().split()))

    res = hanoi(loc)

    fptr.write(str(res) + '\n')

    fptr.close()
