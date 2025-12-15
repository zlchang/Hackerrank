#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counter = {}
    for cc in ar:
        if cc in counter:
            counter[cc] += 1
        else:
            counter[cc] = 1
    pairs = 0
    for cc, nn in counter.items():
        pairs += nn // 2
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
