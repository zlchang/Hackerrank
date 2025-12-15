#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    ff = 0
    bb = 0
    flip = n // 2
    ff = p//2
    bb = flip - ff
        
    if ff > bb:
        return bb
    else:
        return ff
    #
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
