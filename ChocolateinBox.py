#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateInBox' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chocolateInBox(arr):
    # Write your code here
    res = 0
    for a in arr:
        res ^= a
    if res == 0:
        return 0
    cntr = 0
    for a in arr:
        if a^res < a:
            cntr += 1
    return cntr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chocolateInBox(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
