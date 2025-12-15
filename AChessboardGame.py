#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chessboardGame' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
# 
def loop(ii, jj, flag):
    if ii < 1 or ii > 15 or jj < 1 or jj > 15:
        return 1
    elif flag[ii-1][jj-1] != 0:
        return flag[ii-1][jj-1]

    m1 = loop(ii-2, jj+1, flag)
    m2 = loop(ii-2, jj-1, flag)
    m3 = loop(ii+1, jj-2, flag)
    m4 = loop(ii-1, jj-2, flag)
    
    if m1 == 1 and  m2 == 1 and m3 == 1 and m4 == 1:
        flag[ii-1][jj-1] = 2
    elif m1 == 2 or m2 == 2 or m3 == 2 or m4 == 2:
        flag[ii-1][jj-1] = 1
    return flag[ii-1][jj-1]
def chessboardGame(x, y):
    # Write your code here
    n = 15
    flag = [[0 for j in range(n)] for i in range(n)]
    rr = loop(x, y, flag)
    if rr == 1:
        return 'First'
    return 'Second'
                 
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])

        result = chessboardGame(x, y)

        fptr.write(result + '\n')

    fptr.close()
