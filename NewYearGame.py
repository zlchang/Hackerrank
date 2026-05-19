#!/bin/python3

import math
import os
import random
import re
import sys

def NewYearGame(arr):
    marr = []
    for a in arr:
        marr.append(a%3)
    res = 0
    for a in marr:
        res ^= a
    if res == 0:
        return 'Koca'
    return 'Balsa'

if __name__ == '__main__':
    T = int(input().strip())
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for T_itr in range(T):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        # Write your code here
        result = NewYearGame(a)
        fptr.write(result)
        fptr.write('\n')
