#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
 
    if k == 0:
        return range(1, n+1)
    elif n%2 == 0 and (n//2)% k  == 0:
        r = []
        for i in range(n):
            p = 0
            c = i // k
            if c%2 == 0:
                p = i+1+k
            else:
                p = i+1-k
            r.append(p)
        return r
    else:
        return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
