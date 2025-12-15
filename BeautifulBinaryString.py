#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    # Write your code here
    n = len(b)
    if n < 3:
        return 0
    i = 0
    cntr = 0
    while (i < n-2):
        #print(b[i:i+3])
        if b[i:i+3] == '010':
            #print(b[i:i+2])
            i += 3
            cntr += 1
        elif b[i:i+3] == '011':
            i += 3
        else:
            i += 1
    return cntr
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
