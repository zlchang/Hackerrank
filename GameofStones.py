#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def gameOfStones(n):
    # Write your code here
    stones = [0]*100
    stones[0] = 1
    stones[1] = 0
    stones[2] = 0
    stones[3] = 0
    stones[4] = 0
    for ii in range(5, n):
        if stones[ii-2] == 1 or stones[ii-3] == 1 or stones[ii-5] == 1: 
            stones[ii] = 0
        else:
            stones[ii] = 1
    if stones[n-1] == 0:
        return 'First'
    return 'Second'
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
