#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    # Write your code here
    def recursive(X, a):
        #print(X, a)
        if X >= 0 and a == 0:
            return 0
        if X == 0 and a >= 0:
            return 1
        if a**N > X:
            return recursive(X, a-1)
        if a**N == X:
            return recursive(X, a-1)+1
        return recursive(X-a**N, a-1) + recursive(X, a-1)
    return recursive(X, math.floor(math.pow(X, 1/N)))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
