#!/bin/python3

import math
import os
import random
import re
import sys
def KittyandKatty(n):
    if n == 1:
        return 'Kitty'
    if n%2 == 1:
        return 'Katty'
    return 'Kitty'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())
        result = KittyandKatty(n)
        
        fptr.write('{}\n'.format(result))
    fptr.close()
