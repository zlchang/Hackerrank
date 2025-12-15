#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # Write your code here
    nim = 0x0
    n = len(s)
    c = 0
    for i in s:
        nim = nim ^ i
        if i == 1:
            c += 1
            
    if c != n and nim == 0:
        return 'Second'
    elif c == n and nim == 1:
        return 'Second'
    return 'First'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
