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
# The function accepts LONG_INTEGER n as parameter.
#
m = 130
coin = [0]*m
def maxCoin():
    coin[0] = 1
    coin[1] = 1
    coin[2] = 1
    coin[3] = 1
    for i in range(4, m):
        j = 1
        while j*j <= i:
            coin[i] += coin[i-j*j]
            j += 1
def towerBreakers(n):
    # Write your code here
    for i in range(m):
        if coin[i] >= n:
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    maxCoin()
    #print(coin)
    for t_itr in range(t):
        n = int(input().strip())

        result = towerBreakers(n)

        fptr.write(str(result) + '\n')

    fptr.close()
