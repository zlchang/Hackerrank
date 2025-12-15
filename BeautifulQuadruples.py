#!/bin/python3

import os
import sys

sys.setrecursionlimit(10**9)
#
# Complete the beautifulQuadruples function below.
#
def beautifulQuadruples(a, b, c, d):
    #
    # Write your code here.
    #
    n = 3001
    m = 2*n
    arr = [a+1, b+1, c+1, d+1]
    arr.sort()
    
    cntr = [[0 for j in range(n)] for i in range(m)]
    cntr1 = [0 for j in range(n)]
    
    for i in range(1, arr[0]):
        for j in range(i, arr[1]):
            cntr[i^j][j] += 1
            cntr1[j] += 1
    for j in range(m):
        for i in range(2, arr[3]):
            cntr[j][i] += cntr[j][i-1]
    for i in range(2, arr[3]):
            cntr1[i] += cntr1[i-1]
    
    total = 0
    res = 0
    
    for i in range(1, arr[2]):
        for j in range(i, arr[3]):
            total += cntr1[i]
            res += cntr[i^j][i]
    res = total - res
    return res
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    abcd = input().split()

    a = int(abcd[0])

    b = int(abcd[1])

    c = int(abcd[2])

    d = int(abcd[3])

    result = beautifulQuadruples(a, b, c, d)

    fptr.write(str(result) + '\n')

    fptr.close()
