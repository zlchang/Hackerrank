#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nimGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY pile as parameter.
#

def nimGame(pile):
    # Write your code here
    n = len(pile)
    nsum = 0x0
    for ii in range(n):
        nsum = nsum ^ pile[ii]
 
    if nsum != 0x0:
        return 'First'
    return 'Second'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        fptr.write(result + '\n')

    fptr.close()
