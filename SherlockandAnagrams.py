#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    n = len(s)
    cntr = 0
    mm = {}
    sub = [[] for i in range(n)]
    for i in range(n):
        sub[i].append(s[i])
        if mm.get(s[i]) != None:
            cntr += mm[s[i]]
            mm[s[i]] += 1
        else:
            mm[s[i]] = 1
        if i == 0:
            continue
        for ss in sub[i-1]:
            tt = ss+s[i]
            sub[i].append(tt)
            ts = ''.join(sorted(tt))
            if mm.get(ts) != None:
                cntr += mm[ts]
                mm[ts] += 1
            else:
                mm[ts] = 1
    print(mm)
    return cntr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
