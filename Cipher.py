#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING s
#

def cipher(k, s):
    # Write your code here
    if k == 0:
        return s
    n = len(s)
    r = []
    #print(n)
    r.append(ord(s[0])-ord('0'))
    for i in range(1, n-k+1):
        ri = ord(s[i])-ord('0')
        rj = ord(s[i-1])-ord('0')
        ri = rj ^ ri
        if i >= k:
            ri = r[i-k] ^ ri
        r.append(ri)
    res = ''.join(map(str, r))
    return res
            
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = cipher(k, s)

    fptr.write(result + '\n')

    fptr.close()
