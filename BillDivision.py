#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):

    ss = sum(bill)

    pp = (ss - bill[k])/2

    if b > pp:
        return '{:.0f}'.format(b - pp)
    if b == pp:
        return 'Bon Appetit'
    else:
        return '{:.0f}'.format(b - pp)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    result = bonAppetit(bill, k, b)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(result + '\n')
    fptr.close()

