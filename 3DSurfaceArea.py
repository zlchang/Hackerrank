#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    n = len(A)
    m = len(A[0])

    area = 2*n*m

    s1 = 0
    for i in range(n):
        for j in range(m):
            if i == 0:
                s1 += A[i][j]
            else:
                d = A[i][j] - A[i-1][j]
                if d > 0:
                    s1 += d
    s2 = 0
    for i in range(n-1, -1, -1):
        for j in range(m):
            if i == n-1:
                s2 += A[i][j]
            else:
                d = A[i][j] - A[i+1][j]
                if d > 0:
                    s2 += d
    s3 = 0
    for j in range(m):
        for i in range(n):
            if j == 0:
                s3 += A[i][j]
            else:
                d = A[i][j] - A[i][j-1]
                if d > 0:
                    s3 += d
    s4 = 0
    for j in range(m-1, -1, -1):
        for i in range(n):
            if j == m-1:
                s4 += A[i][j]
            else:
                d = A[i][j] - A[i][j+1]
                if d > 0:
                    s4 += d
    return area+s1+s2+s3+s4

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
