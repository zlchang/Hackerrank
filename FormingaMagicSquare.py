#!/bin/python3

import math
import os
import random
import re
import sys

def cost(s, sc):
    cc = 0
    for i in range(len(sc)):
        for j in range(len(sc[i])):
            cc = cc + abs(sc[i][j]-s[i][j])
    return cc
def generate(a, b):
    xx = []
    sc = [[0 for i in range(3)] for j in range(3)]
    sc[0][0] = a
    sc[0][1] = b
    sc[1][1] = 5
    #print(a, b)
    sc[0][2] = 15 - sc[0][0] - sc[0][1]
    sc[2][2] = 10 - sc[0][0]
    sc[2][1] = 10 - sc[0][1]
    sc[2][0] = 10 - sc[0][2]
    sc[1][0] = 15 - sc[0][0] - sc[2][0]
    sc[1][2] = 10 - sc[1][0]
    
    for i in range(3):
        for j in range(3):
            if sc[i][j] in xx or sc[i][j] < 1 or sc[i][j] > 9:
                return [[0]*3]*3
            else:
                xx.append(sc[i][j])
            
    #print(sc)
    return sc

def formingMagicSquare(s):
    nn = [1, 2, 3, 4, 6, 7, 8, 9]
    mm = 81
    for i in range(len(nn)-1):
        a = nn[i]
        j = i+1
        while j < len(nn):
            b = nn[j]
            #if a+b == 10 or a+b > 14 or a+b < 6 or 15-a-b == a or 15-a-b == b:
                #j += 1
                #continue
            #else:
                #print(a, b)
            s1 = generate(a,b)
                #print(s1)
            c1 = 81
            if s1[0][0] != 0:
                c1 = cost(s, s1)
            c2 = 81
            s2 = generate(b, a)
            if s2[0][0] != 0:
                c2 = cost(s, s2)
                    #c2 = 99
            cc = min(c1, c2)
            if cc < mm:
                mm = cc
            j += 1
    return mm

# Complete the formingMagicSquare function below.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
