#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    n = len(x)
    x.sort()
    start = x[0]
    tower = x[0]
    end = x[0]+k
    cntr = 1
    for i in range(1, n):
        tt = x[i]
        if tt > end:
            start = tt
            tower = tt
            end = tt+k
            cntr += 1
        else:
            if start+k >= tt:
                tower = tt
                end = tt+k
        #print(start, tower, end)
    return cntr
    
            
         
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
