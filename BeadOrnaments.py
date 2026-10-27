#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beadOrnaments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY b as parameter.
#
mod = 1000000007
def beadOrnaments(b):
    # Write your code here
    n = len(b)
    print(10**0, int(math.pow(10, 0)))
    if n == 1:
        if b[0] == 1:
            return 0
        return (b[0]**(b[0]-2))%mod
    sumb = 0
    res = 1
    for bi in b:
        res *= bi**(bi-1)
        res %= mod
        sumb += bi
        sumb %= mod
    res = (res*(sumb**(n-2)))%mod
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        b_count = int(input().strip())

        b = list(map(int, input().rstrip().split()))

        result = beadOrnaments(b)

        fptr.write(str(result) + '\n')

    fptr.close()
