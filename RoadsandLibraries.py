#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    edges = [[] for i in range(n)]
    for a, b in cities:
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    #print(edges)
    visited = [0]*n
    cntr = 0
    cost = 0
    for i in range(n):
        nodes = 0
        if visited[i] == 0:
            qq = []
            qq.append(i)
            visited[i] = 1
            nodes += 1
            while qq != []:
                q = qq.pop(0)
                for e in edges[q]:
                    if visited[e] == 0:
                        qq.append(e)
                        visited[e] = 1
                        nodes += 1
            
            cntr += 1
            if c_lib > c_road:
                cost += c_lib+(nodes-1)*c_road
            else:
                cost += c_lib*nodes
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
