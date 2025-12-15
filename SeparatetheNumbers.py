#!/bin/python3

import math
import os
import random
import re
import sys

def check(a, h, s):
    i = h
    n = len(s)
    if h == n: return True
    if s[h] == '0': return False
    v = 0
    while i < n and v < a:
        v = v * 10 + int(s[i])
        i += 1
    #print(v)
    return v == a and check(a+1, i, s)
# Complete the separateNumbers function below.
def separateNumbers(s):
    n = len(s)
    l = n // 2
    if s[0] == '0': return 'NO'
    for i in range(1, l+1):
        a = 0
        j = 0
        while j < i:
            a = a * 10 + int(s[j])
            j += 1
        print(i, a)
        if check(a+1, j, s):
            return 'YES {:d}'.format(a)
    return 'NO'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        s = input()

        r = separateNumbers(s)
        fptr.write(''.join(r))
        fptr.write('\n')
