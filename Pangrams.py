#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    n = len(s)
    cntr = [0]*26
    for i in range(n):
        if ord(s[i]) == ord(' '): continue
        a = ord(s[i])
        if a >= ord('a') and a <= ord('z'):
            cntr[a-ord('a')] = 1
        elif a >= ord('A') and a <= ord('Z'):
            cntr[a-ord('A')] = 1
    s = sum(cntr)
    if s == 26:
        return 'pangram'
    return 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
