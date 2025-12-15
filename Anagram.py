#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    n = len(s)
    if n%2 == 1:
        return -1
    else:
        cntr = {}
        for i in range(0,n):
            if i < n/2:
                if s[i] in cntr:
                    cntr[s[i]] += 1
                else:
                    cntr[s[i]] = 1
            else:
                if s[i] in cntr and cntr[s[i]] > 0:
                    cntr[s[i]] -= 1
        return sum(cntr.values())
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
