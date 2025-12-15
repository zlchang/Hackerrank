#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):

    c = 'hackerrank'
    n = len(s)
    m = len(c)
    j = 0
    for i in range(n):
        if j < m and s[i] == c[j]:
            j += 1
    if j == m:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
