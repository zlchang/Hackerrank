#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    cntr = 0
    n = len(q)
    for i in range(n-1, -1, -1):
        if q[i]-1 - i > 2:
            print(i, q[i])
            return 'Too chaotic'
        elif q[i]-1 == i:
            continue
        elif i > 0 and q[i-1]-1 == i:
            q[i-1] = q[i]
            q[i] = i+1
            cntr += 1
        elif i > 1 and q[i-2]-1 == i: 
            q[i-2] = q[i-1]
            q[i-1] = q[i]
            q[i] = i+1
            cntr += 2 
        #print(i, q)
    return str(cntr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        result = minimumBribes(q)
        fptr.write(result+'\n')
    
    fptr.close()
