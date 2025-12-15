#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    nr = len(container)
    nc = len(container[0])
    #print(nr, nc)
    sr = [0]*nr
    sc = [0]*nc
    for i in range(nr):
        for j in range(nc):
            sr[i] += container[i][j]
            sc[j] += container[i][j]

    for i in range(nr):
        ff = 0
        for j in range(nc):
            ff += sr[i] == sc[j]
        if ff == 0:
            return 'Impossible'
    for j in range(nc):
        ff = 0
        for i in range(nr):
            ff += sr[i] == sc[j]
        if ff == 0:
             return 'Impossible'
            
    return 'Possible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
