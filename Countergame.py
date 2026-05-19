#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    cntr = 0
    index = -1
    i = 0
    while (n >> i) != 0:
        b = (n >> i) & 0x1
        if b == 1:
            cntr += 1
        if cntr == 1 and index == -1:
            index = i   
        i += 1
    print(index, cntr)    
    win = (index+cntr) % 2
    
    if win == 0:
        return 'Louise'
    return 'Richard'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
