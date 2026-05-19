#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theGreatXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER x as parameter.
#

def theGreatXor(x):
    # Write your code here
    if x <= 1:
        return 0
    cntr = 0
    res = 0
    while x >> cntr:
        if (x >> cntr) & 0x1 == 0:
            res += (1 << cntr)  
        cntr += 1
   
    return res

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        x = int(input().strip())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()
