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
# The function accepts 2D_INTEGER_ARRAY coins as parameter.
#
n = 15
memo = [[-1 for i in range(n)] for j in range(n)]
def grundy(x, y):

    if memo[x-1][y-1] != -1:
        return memo[x-1][y-1]
    state = set()
    if x-2 >= 1 and x-2 <= n:
        if y+1 >= 1 and y+1 <= n:
            state.add(grundy(x-2, y+1))
        if y-1 >= 1 and y-1 <= n:
            state.add(grundy(x-2, y-1))
    if y-2 >= 1 and y-2 <= n:
        if x+1 >= 1 and x+1 <= n:
            state.add(grundy(x+1, y-2))
        if x-1 >= 1 and x-1 <= n:
            state.add(grundy(x-1, y-2)) 
    i = 0
    while i in state:
        i += 1
    memo[x-1][y-1] = i
    return i 
def chessboardGame(coins):
    # Write your code here
    res = 0
    for x, y in coins:
        g = memo[x-1][y-1]
        res ^= g
    #print(memo)
    if res == 0:
        return 'Second'
    return 'First'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            grundy(i, j)

    for t_itr in range(t):
        k = int(input().strip())

        coins = []

        for _ in range(k):
            coins.append(list(map(int, input().rstrip().split())))

        result = chessboardGame(coins)

        fptr.write(result + '\n')

    fptr.close()
