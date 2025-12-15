#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    m = int(d/2)
    trail = [0]*201
    n = len(expenditure)
    counter = 0
    for i in range(n):
        e = expenditure[i]
        if i >= d:
            #print(trail)
            s = 0
            b = 0
            c = 0
            for j in range(201):
                if trail[j] > 0:
                    c += trail[j]
                if d%2 == 1 and c >= m+1:
                    s = j
                    break
                elif c == m:
                    s = j
                    b = 1
                    print(c, j)
                elif c > m:
                    if b == 1:
                        s += j
                        s /= 2
                        
                    else:
                        s = j
                    break    
                    
            #print(e, s)
            if e >= 2*s:
                counter += 1
            f = expenditure[i-d]
            trail[f] -= 1
        trail[e] += 1
    return counter
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
