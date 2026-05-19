#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anotherMinimaxProblem' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
node = 0
def add(trie, root, x, nbs):
    global node
    curr = root
    #print(f'nbs={nbs}')
    for i in range(nbs-1, -1, -1):
        bi = (x >> i) & 0x1
        #print(i, bi, trie[curr][bi])
        if trie[curr][bi] > 0:
            curr = trie[curr][bi]
        else:
            node += 1
            trie[curr][bi] = node
            #print(curr, bi, node)
            curr = node
def get(trie, root, x, nbs):
    val = 0x0
    curr = root
    for i in range(nbs-1, -1, -1):
        bi = (x >> i) & 0x1
        #print(i, curr, bi, trie[curr][bi])
        if trie[curr][bi] == 0:
            val = val | (1 << i)
            curr = trie[curr][(bi+1)%2]
        else:
            curr = trie[curr][bi]
    return val
def anotherMinimaxProblem(a):
    # Write your code here
    n = len(a)
    a.sort()
    mask = a[0]^a[n-1]
    nbits = mask.bit_length()
    if mask == 0x0:
        return 0
    #print(bin(mask), nbits)
    m = n*(nbits+1)
    lower = [[0 for i in range(2)] for j in range(m)]
 
    res = float('inf')
    for i in range(n):
        if (a[i] >> (nbits-1)) & 0x1 == 0:
            #print(a[i])
            add(lower, 0, a[i], nbits)
        else:
            xor = get(lower, 0, a[i], nbits)
            #print(bin(a[i]), xor)
            res = min(res, xor)
    return res
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = anotherMinimaxProblem(a)

    fptr.write(str(result) + '\n')

    fptr.close()
