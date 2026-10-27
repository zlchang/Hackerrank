#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverseShuffleMerge(s):
    # Write your code here
    cntr = [0 for _ in range(26)]
    for si in s:
        i = ord(si) - ord('a')
        cntr[i] += 1
    res = []
    need = [0 for _ in range(26)]
    for i in range(26):
        need[i] = cntr[i]//2
    temp = [0 for _ in range(26)]
    for si in s[::-1]:
        i = ord(si)-ord('a')
        temp[i] += 1
        if need[i] == 0:
            continue
        while res:
            top = res[-1]
            j = ord(top) - ord('a')
            if top > si and need[i] > 0 and cntr[j] - temp[j] > need[j]:
                res.pop()
                need[j] += 1
            else:
                break
        res.append(si)
        need[i] -= 1
   
    return "".join(res)
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
