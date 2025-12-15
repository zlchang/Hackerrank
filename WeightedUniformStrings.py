#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    n = len(s)
    f = [0]*(26*n)
    w = []
    c = 0
    for i in range(n):
        u = ord(s[i]) - ord('a') + 1
        if i > 0 and s[i] == s[i-1]:
            c += u
        else:
            c = u
        #if c not in w:
        f[c-1] = 1
    r = []
    for q in queries:
        if q <= 26*n and f[q-1]:
            r.append('Yes')
        else:
            r.append('No')
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
