#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def nfactor(x):
    nf = 0
    while x % 2 == 0:
        x = x // 2
        nf += 1
    i = 3
    while i*i <= x:
        while x % i == 0:
            x = x // i
            nf += 1
        i += 2
    if x > 2:
        nf += 1
    return nf
        
def towerBreakers(arr):
    # Write your code here
    cntr = 0
    for a in arr:
        if a > 1:
            cntr = cntr ^ nfactor(a)
    if cntr == 0:
        return 2
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    
    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = towerBreakers(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
