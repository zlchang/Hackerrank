#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the xorSequence function below.
def xorSequence(l, r):
    a = l // 4
    b = r // 4
    sor = 0
    prev = 0
    for i in range(3):
        curr = prev^(4*a+i)
        if 4*a+i >= l and 4*a+i <= r:
            sor ^= curr
        prev = curr
    if b > a:
        prev = 0
        for i in range(3):
            curr = prev^(4*b+i)
            if 4*b+i <= r:
                sor ^= curr
            prev = curr
        if (b-a) % 2 == 0:
            sor ^= 2
    return sor
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
