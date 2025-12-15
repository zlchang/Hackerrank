#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nimbleGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def nimbleGame(s):
    # Write your code here
    nim = 0x0
    n = len(s)
    for i in range(1, n):
        if s[i] % 2 == 1:
            nim = nim ^ i
    if n > 1 and nim != 0x0:
        return 'First'
    return 'Second'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = nimbleGame(s)

        fptr.write(result + '\n')

    fptr.close()
