#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'half' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def half(n):
    # Write your code here
    if n%2 == 1:
        return 1
    bc = n.bit_length()
    #print(bc)
    gr = 1^bc
    bc = 1 << (gr.bit_length()-1)
    print('bc={} gr={}'.format(bc, gr))
    if bc - (bc^gr) == 1:
        return 1 << (bc-2)
    res = (1 <<(bc-1)) - ((1<< (bc^gr))-1)
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = half(n)

        fptr.write(str(result) + '\n')

    fptr.close()
