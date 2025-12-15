#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    # Write your code here
    mod = 1000000007
    m = 26
    arr1 = [0]*m
    arr2 = [[0 for i in range(m)] for j in range(m)]
    arr3 = [0]*m
    
    res = 0
    
    for ss in s:
        i = ord(ss)-ord('a')         
        res += arr3[i]
        res = res % mod
        for j in range(m):
            arr3[j] += arr2[j][i]
        for j in range(m):
            arr2[j][i] += arr1[j]
        arr1[i] += 1
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
