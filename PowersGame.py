#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powersGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def powersGame(n):
    # Write your code here
    #sp = 1
    #for i in range(1, 9):
        #sp *= 2
        #print(sp%17)
    if n % 8 == 0:
        return 'Second'
    return 'First'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = powersGame(n)

        fptr.write(result + '\n')

    fptr.close()
