#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    ns = len(s)

    count = [0]*(ns+1)
    count[0] = 0
    for i in range(ns):
        if s[i] == 'a':
            count[i+1] = count[i] + 1
        else:
            count[i+1] = count[i]

    q = n//ns
    m = n%ns

    return q*count[ns]+count[m]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
