#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    n1 = len(s1)
    n2 = len(s2)
    
    counts = [[0 for j in range(n2+1)] for i in range(n1+1)]
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                counts[i][j] = counts[i-1][j-1]+1
            else:
                counts[i][j] = max(counts[i-1][j], counts[i][j-1])
            
            
    return counts[n1][n2]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
