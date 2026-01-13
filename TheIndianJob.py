#!/bin/python3

import os
import sys

#
# Complete the indianJob function below.
#
def indianJob(g, arr):
    #
    # Write your code here.
    #
    n = len(arr)
    sa = sum(arr)
    prev = [0]*(sa+1)
    prev[0] = 1
    curr = [0]*(sa+1)
    for x in arr:
        for i in range(sa+1):
            if i < x:
                curr[i] = prev[i]
            else:
                curr[i] = prev[i] or prev[i-x]
        prev = list(curr)
    for i in range(sa+1):
        if prev[i] and sa-i <= g and i <= g:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ng = input().split()

        n = int(ng[0])

        g = int(ng[1])

        arr = list(map(int, input().rstrip().split()))

        result = indianJob(g, arr)

        fptr.write(result + '\n')

    fptr.close()
