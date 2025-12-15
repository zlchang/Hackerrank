#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    l = list(s)
    c = [0]*n
    i = 0
    j = n-1
    m = 0
    while i <= j:
        if l[i] != l[j]:
            if ord(l[i])-ord('0') > ord(l[j])-ord('0'):
                l[j] = l[i]
            else: 
                l[i] = l[j]
            c[i] = 1
            c[j] = 1
            m += 1
        i += 1
        j -= 1
    if k < m:
        return '-1'
    k = k-m
    i = 0
    j = n-1
    while i <= j:
        print(k, l[i])
        if k > 0 and l[i] != '9':
            if c[i] == 1:
                l[i] = '9'
                l[j] = '9'
                k -= 1
            if c[i] == 0 and k > 1:
                l[i] = '9'
                l[j] = '9'
                k -= 2
            if i == j:
                l[i] = '9'
                k -= 1
        i += 1
        j -= 1
            
    return ''.join(l)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
