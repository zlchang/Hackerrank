#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

    
def permutationGame(arr):
    # Write your code here
    n = len(arr)
    m = (1<<n)-1
    memo = [-1]*(m+1)
    def grundy(mask):
        flag = False
        if memo[mask] != -1:
            return memo[mask]
        if mask.bit_count() == 1:
            memo[mask] = 0
            return 0
        prev = -1
        for i in range(n):
            if (mask >> i) & 0x1:
                if prev != -1:
                    if arr[i] < arr[prev]:
                        flag = True
                        break
                prev = i

        #print(arr)
        #print(flag)
        if not flag:
            memo[mask] = 0
            return 0
        gr = set()
        for i in range(n):
            if (mask >> i) & 0x1:
                nmask = mask ^ (1 << i)
                gr.add(grundy(nmask))
        i = 0
        #print(gr)
        while i in gr:
            i += 1
        #print(i)
        memo[mask] = i
        return i
    res = grundy(m)
    if res == 0:
        return 'Bob'
    return 'Alice'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = permutationGame(arr)

        fptr.write(result + '\n')

    fptr.close()
