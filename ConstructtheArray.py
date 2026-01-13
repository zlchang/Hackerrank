#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    mod = 1000000007
    prev_a = 0
    prev_b = 1
    
    for i in range(2,n):
        curr_a = 0
        curr_b = 0
        
        curr_a = (k-1)*prev_b % mod
        curr_b = (prev_a+(k-2)*prev_b) % mod
        
        prev_a = curr_a
        prev_b = curr_b
    
    if x == 1:
        return prev_a
    
    return prev_b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
