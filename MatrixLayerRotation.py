#!/bin/python3

import math
import os
import random
import re
import sys

def circle(a, b, matrix, r):
    rs = len(matrix)
    cs = len(matrix[0])
    arr = []
    for i in range(a-1, rs-a+1):
        arr.append(matrix[i][cs-b])
    for i in range(cs-b+1, b):
        arr.append(matrix[rs-a][i])
    for i in range(rs-a-1, a-2, -1):
        arr.append(matrix[i][b-1])
    for i in range(b-2, cs-b, -1):
        arr.append(matrix[a-1][i])
    #print(arr)
    n = len(arr)
    brr = [0]*n
    for i in range(n):
        j = (i+r)%n
        #print(j)
        brr[j] = arr[i]
    cntr = 0
    #print(brr)
    for i in range(a-1, rs-a+1):
        matrix[i][cs-b] = brr[cntr]
        cntr += 1
    for i in range(cs-b+1, b):
        matrix[rs-a][i] = brr[cntr]
        cntr += 1
    for i in range(rs-a-1, a-2, -1):
        matrix[i][b-1] = brr[cntr]
        cntr += 1
    for i in range(b-2, cs-b, -1):
        matrix[a-1][i] = brr[cntr]
        cntr += 1
        
    
# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    rs = len(matrix)
    cs = len(matrix[0])
    i = 1
    j = cs
    cntr = 0
    while i <= rs//2 and j > cs // 2:
        cntr += 1
        circle(i, j, matrix, r)
        i += 1
        j -= 1
    #print(cntr)
    return matrix

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    result = matrixRotation(matrix, r)
    for i in range(m):
     fptr.write(' '.join(map(str, result[i])))
     fptr.write('\n')
