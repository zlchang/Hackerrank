#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    counter = [0]*26
    for i in s:
        j = ord(i)-ord('a')
        counter[j] += 1
    ss = 0
    sc = 0
    mm = 0
    for c in counter:
        ss += c
        if c > 0:
            sc += 1
        if c > mm:
            mm = c 
    if ss == mm*sc or ss == (mm-1)*sc+1 or ss == 1+mm*(sc-1):
        return 'YES'
    return 'NO'
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
