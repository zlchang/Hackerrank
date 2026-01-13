#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'playWithWords' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def playWithWords(s):
    # Write your code here
    n = len(s)
    lps = [[0]*n for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if j == i:
                lps[i][j] = 1
            else:
                if s[i] == s[j]:
                    lps[i][j] = lps[i+1][j-1] + 2
                else:
                    lps[i][j] = max(lps[i+1][j], lps[i][j-1])
    #print(lps)
    res = 0
    for i in range(n-1):
        res = max(res, lps[0][i]*lps[i+1][n-1])
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = playWithWords(s)

    fptr.write(str(result) + '\n')

    fptr.close()
