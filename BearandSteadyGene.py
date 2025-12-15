#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steadyGene(gene):
    # Write your code here
    n = len(gene)
    m = n // 4
    counts = {'A':0, 'C': 0, 'G':0, 'T':0}
    for g in gene:
        counts[g] += 1
    s = True
    for k in counts.keys():
        s = s and counts[k] == m
    if s:
        return 0
    r = n
    i = 0
    for j in range(n):      
        counts[gene[j]] -= 1
        f = True
        for k in counts.keys():
            f = f and counts[k] <= m
        while f:
            r = min(r, j-i+1)
            counts[gene[i]] += 1
            i += 1       
            for k in counts.keys():
                f = f and counts[k] <= m
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
