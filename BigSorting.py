#!/bin/python3

import math
import os
import random
import re
import sys
import functools

def compare(a, b):
    na = len(a)
    nb = len(b)
    if na > nb: return 1
    elif na < nb: return -1
    else:
        for i in range(na):
            ai = a[i]
            bi = b[i]
            if ai > bi:
                return 1
            elif ai < bi:
                return -1
    return 0
# Complete the bigSorting function below.
def bigSorting(unsorted):
    return sorted(unsorted, key=functools.cmp_to_key(compare))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
