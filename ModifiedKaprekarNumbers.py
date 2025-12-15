#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    res = []
    for i in range(p,q+1):
        r = i
        s = r*r
        m = 10
        while r // 10 != 0:
            m *= 10
            r = r//10
        a = s // m
        b = s % m
        if a+b  == i:
            res.append(i)
    if len(res) == 0:
        res.append('INVALID RANGE')
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    p = int(input())

    q = int(input())

    result = kaprekarNumbers(p, q)
    fptr.write(' '.join(map(str, result))+'\n')

    fptr.close()


