#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stoneDivision' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER_ARRAY s
#
#sys.setrecursionlimit(100000)
def stoneDivision(n, s):
    # Write your code here
    memo = {}
    def recursive(nn):
        if nn in memo:
            return memo[nn]
        cntr = 0
        for si in s:
            if nn%si == 0 and nn > si:
                m = nn//si
                ci = 1 + m*recursive(si)
                if ci > cntr:
                    cntr = ci
        memo[nn] = cntr
        return cntr
    return recursive(n)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = list(map(int, input().rstrip().split()))

        result = stoneDivision(n, s)

        fptr.write(str(result) + '\n')

    fptr.close()
