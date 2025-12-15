#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    counter = {}

    for v in a:
        if v in counter:
            counter[v] += 1
        else:
            counter[v] = 1
    
    ss = sorted(counter)

    mm = ss[0]
    if len(ss) == 1:
        return counter[mm]
    else:
        length = []
        for i in range(1, len(ss)):
            s = ss[i]
            l = counter[s]
            if s - mm == 1:
                length.append(l+counter[mm])
            else:
                length.append(counter[mm])
                if i == len(ss)-1:
                    length.append(l)
            mm = s
        return max(length)

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
