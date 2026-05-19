#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'zeroMoveNim' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def zeroMoveNim(p):
    # Write your code here
    n = len(p)
    xor = 0
    for i in p:
        j = i+1
        if i % 2 == 0:
            j = i-1
        xor ^= j
    if xor == 0:
        return 'L'
    return 'W'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())
        
        p = list(map(int, input().rstrip().split()))

        result = zeroMoveNim(p)

        fptr.write(result + '\n')

    fptr.close()
