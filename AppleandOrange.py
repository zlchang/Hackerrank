#!/bin/python3

import math
import os
import random
import re
import sys

def counter(s, t, a, apples):
    cntr = 0
    for d in apples:
        if a+d >= s and a+d <= t:
            cntr += 1
    return cntr

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    res = []
    res.append(counter(s,t, a, apples))
    res.append(counter(s,t, b, oranges))
    print(*res, sep='\n')

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
