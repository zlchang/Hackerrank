#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    n = len(s)
    m = n//2
    print(m)
    for i in range(m):
        print(s[i])
        if s[i] != s[n-1-i]:
            if i== m-1:
                return i
            elif s[i+1] == s[n-1-i] and s[i+2] == s[n-1-i-1]:
                return i
            elif s[i] == s[n-1-i-1] and s[n-1-i-2] == s[i+1]:
                return n-1-i
    return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
