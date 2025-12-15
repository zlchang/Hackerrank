#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    n = len(p)
    f = {}
    for i in range(n):
        if p[i] not in f:
            f[p[i]] = i+1
    r = []

    for i in range(n):
        j = i+1
        r.append(f[f[j]])
    
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
