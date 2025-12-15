#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    n = len(s)
    counter = [0]*26
    for i in range(0, n):
        index=ord(s[i])-ord('a')
        counter[index] += 1
    flag = 0
    for i in range(0, 26):
            if(counter[i]%2):
                flag += 1
    if n%2 == 0 and flag == 0:
        return 'YES'
    elif n%2 == 1 and flag == 1:
        return 'YES'
    else:
        return 'NO'
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
