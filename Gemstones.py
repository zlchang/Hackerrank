#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):

    count = [0]*26
    n = len(arr)
    for i in range(n):
        cc = [0]*26
        stone = arr[i]
        m = len(stone)
        for j in range(m):
            k = ord(stone[j])-ord('a')
            if cc[k] == 0:
                cc[k] = 1
                #print(k, cc[k])
        for k in range(26):
            count[k] += cc[k]
    result = 0
    for i in range(26):
        if count[i] == n:
            result += 1
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
