#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    m = ['S', 'O', 'S']
    n = len(s)
    cntr = 0
    for i in range(n):
        j = i % 3
        if s[i] != m[j]:
            cntr += 1
    return cntr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
