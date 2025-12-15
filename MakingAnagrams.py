#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    a1 = [0]*26
    for ss in s1:
        ii = ord(ss)-ord('a')
        a1[ii] += 1
        
    a2 = [0]*26
    for ss in s2:
        ii = ord(ss)- ord('a')
        a2[ii] += 1
    cntr = 0
    for ii in range(0,26):
        cntr += abs(a1[ii]-a2[ii])
    return cntr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
