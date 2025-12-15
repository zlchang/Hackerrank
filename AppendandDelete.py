#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    ns = len(s)
    nt = len(t)

    i = 0

    while i < ns and i < nt and s[i] == t[i]:
        i += 1
    
    np = nt - i + ns - i
    print(i)
    if k < np:
        return 'No'
    elif (k - np)%2 == 0 or k > np + 2*i:
        return 'Yes'   
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
