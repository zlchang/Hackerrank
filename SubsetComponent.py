#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'findConnectedComponents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY d as parameter.
#

def findConnectedComponents(d):
    # Write your code here
    n = len(d)
    m = 1 << n
    res = 0
    bitmap = defaultdict(int)
    for i in range(m):
        graphs = []
        j = 0
        while (i >> j):
            if (i >> j) & 0x1:
                dj = d[j]
                k = 0
                ng = len(graphs)
                while k < ng:
                    if graphs[k] & dj:
                        graphs[k] = graphs[k] | dj
                        if graphs[k] not in bitmap:
                            bitmap[graphs[k]] = graphs[k].bit_count()
                        break
                    k += 1
                if k == ng:
                    graphs.append(dj)
                    bitmap[graphs[k]] = dj.bit_count()
            j += 1
        bit = 0
        ng = len(graphs)
        for g in graphs:
            bit |= g
        if bit not in bitmap:
            bitmap[bit] = bit.bit_count()
        res += ng+64-bitmap[bit]
        #if i == 7:
            #print(ng, bit, bitmap[bit])
        #print(i, ng+64-bitmap[bit])
    return res
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d_count = int(input().strip())

    d = list(map(int, input().rstrip().split()))

    components = findConnectedComponents(d)

    fptr.write(str(components) + '\n')

    fptr.close()
