#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summingPieces' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def summingPieces(arr):
    # Write your code here
    mod = 1000000007
    n = len(arr)
    p2 = [1]*n #a_i = sum_{j=0}^{i-1} 2*pow(i-j-1)
    bf = [0]*n #b_i = sum_{j=0}^{i-1} (j+1)*2**pow(i-j-1)
    for i in range(1, n):
        p2[i] = (1+2*p2[i-1]) % mod
        bf[i] = (bf[i-1]+p2[i-1]) % mod
    #print(bf)
    asum = [0]*n # asum_i sum_i v_i*a_{i-1}
    bsum = [0]*n # bsum_i = bsum_{i-1} + v_i*b_i + asum_{i-1} with i > 0
    csum = [0]*n # csum_i = sum_i v_i
    csum[0] = arr[0]
    for i in range(1, n):
        asum[i] = (asum[i-1]+p2[i-1]*arr[i]) % mod
        bsum[i] = (bsum[i-1]+asum[i-1]+bf[i]*arr[i]) % mod
        csum[i] = (csum[i-1] + arr[i]) % mod
    
    psum = [0]*n
    psum[0] = bsum[0]+csum[0]
    for i in range(1, n):
        psum[i]= (2*psum[i-1]+bsum[i]+(i+1)*csum[i]-(bsum[i-1]+i*csum[i-1])) % mod
  
    
    res = psum[n-1]
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = summingPieces(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
