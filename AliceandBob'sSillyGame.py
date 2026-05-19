#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sillyGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#
nmax = 10**5
prime = [1]*(nmax+1)
def sieve(prime):
    prime[0] = 0
    prime[1] = 0
    i = 2
    while i*i <= nmax:
        if prime[i]:
            j = i*i
            while j <= nmax:
                prime[j] = 0
                j += i
        i += 1
def sillyGame(n):
    # Write your code here
    cntr = 0
    for i in range(2, n+1):
        if prime[i]:
            cntr += 1
        
    if cntr % 2 == 0:
        return 'Bob'
    return 'Alice'
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())
    sieve(prime)
    for g_itr in range(g):
        n = int(input().strip())

        result = sillyGame(n)

        fptr.write(result + '\n')

    fptr.close()
