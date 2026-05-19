#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bobAndBen' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY trees as parameter.
#

def bobAndBen(trees):
    # Write your code here
    res = 0
    for m, k in trees:
        if m != 2:
            res ^= 1+(m-1)%2
    if res == 0:
        return 'BEN'
    return 'BOB'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        trees = []

        for _ in range(n):
            trees.append(list(map(int, input().rstrip().split())))

        result = bobAndBen(trees)

        fptr.write(result + '\n')

    fptr.close()
