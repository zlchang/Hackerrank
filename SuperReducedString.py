#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    n = len(s)
    ss = []
    for i in range(n):
        if len(ss) == 0 or ss[-1] != s[i]:
            ss.append(s[i])
        else:
            ss.pop()
    if len(ss) == 0:
        return 'Empty String'
    aa =''
    for a in ss:
        aa += a
    return aa

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
