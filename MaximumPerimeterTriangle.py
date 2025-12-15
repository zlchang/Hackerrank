#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort(reverse=True)
    n = len(sticks)
    arr = []
    if n < 3:
        arr = [-1]
    else:
        for ii in range(n-2):
            aa = sticks[ii]
            bb = sticks[ii+1]
            cc = sticks[ii+2]
            if bb+cc > aa:
                arr = [cc, bb, aa]
                return arr
    arr = [-1]
    return arr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
