#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    # Write your code here
    edges = [[] for i in range(n)]
    for a, b in astronaut:
        edges[a].append(b)
        edges[b].append(a)
        
    visited = [0 for i in range(n)]
    numbers = []
    for i in range(n):
        if visited[i] == 1:
            continue
        qq = []
        qq.append(i)
        visited[i] = 1
        num = 1
        while qq != []:
            q = qq.pop(0)
            for e in edges[q]:
                if visited[e] == 1:
                    continue
                qq.append(e)
                visited[e] = 1
                num += 1
        numbers.append(num)
    
    l = len(numbers)
    res = n*(n-1)
    for i in range(l):
        res -= numbers[i]*(numbers[i]-1)
    return res//2
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
