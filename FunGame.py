#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funGame' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def funGame(a, b):
    # Write your code here
    s = [(x+y, x, y) for x, y in zip(a, b)]
    s.sort(key=lambda x: x[0], reverse=True)
    #print(s)
    first = 0
    second = 0
    for i in range(len(s)):
        if i % 2 == 0:
            first += s[i][1]
        else:
            second += s[i][2]
    if first == second:
        return 'Tie'
    if first > second:
        return 'First'
    return 'Second'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = funGame(a, b)

        fptr.write(result + '\n')

    fptr.close()
