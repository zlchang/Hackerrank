#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Write your code here
    n = len(s)
    m = n//2
    cntr = 0
    for i in range(0, m):
        l = ord(s[i]) - ord('a')
        k = ord(s[n-i-1]) - ord('a')
        #print("i={} s={}".format(i, s[i]))
        cntr += abs(l-k)
    return cntr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
