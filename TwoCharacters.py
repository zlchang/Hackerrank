#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    letters = []
    for i in range(len(s)):
        if s[i] not in letters:
            letters.append(s[i])
    if len(letters) == 1: return 0
    res = []
    for i in range(len(letters)-1):
        for j in range(i+1, len(letters)):
            a = letters[i]
            b = letters[j]
            p = ''
            cntr = 0
            for k in range(len(s)):
                if s[k] == a or s[k] == b:
                    #print(p)
                    if p != s[k]:
                        p = s[k]
                        cntr += 1
                    else:
                        cntr = 0
                        break
            #if cntr > 0: print(a, b)
            res.append(cntr)
    return max(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
