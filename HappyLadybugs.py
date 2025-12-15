#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    count = {}
    n = len(b)
    if n == 1 and b[0] != '_':
        return 'NO'
    for i in range(len(b)):
        if b[i] not in count:
            count[b[i]] = 1
        else:
            count[b[i]] += 1
    for k, v in count.items():
        if k != '_' and v == 1:
            return 'NO'
    if '_' not in count:
        for i in range(n):
            if i == 0 and b[i] != b[i+1]:
                return 'NO'
            elif i == n-1 and b[i] != b[i-1]:
                return 'NO'
            elif b[i] != b[i-1] and b[i] != b[i+1]:
                return 'NO'
    return 'YES' 

        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
