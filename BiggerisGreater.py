#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    n = len(w)
    s = ''+w[n-1]
    for i in range(n-2, -1, -1):
        c = w[i]
        p = w[i+1]
        if c >= p:
            s += c
        else:
            r = ''
            for j in range(i):
                r += w[j]
            k = 0
            while k < len(s)-1:
                if s[k] > c:
                    break
                k += 1
            r += s[k]
            r += s[0:k]
            r += c
            r += s[k+1::]
            return r
    
    return 'no answer'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
