#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**9)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        # Write your code here
        cmax = [0]*(l+1)
        cmin = [0]*(l+1) 
        for i in range(1, l+1):
            cmax[i] = i-1+cmax[i-1]
            mid = i//2
            cmin[i] = i-1+cmin[mid]+cmin[i-1-mid]
        #print(cmax)
        #print(cmin)
        res = []
        def solve(offset, nl, nc):
            if nl == 0:
                return
            if nl == 1:
                res.append(offset)
                return 
            pivot = 0
            nc -= nl-1   
            while cmax[pivot]+cmax[nl-1-pivot] < nc or cmin[pivot]+cmin[nl-1-pivot] > nc:
                pivot += 1
            
            res.append(offset+pivot)
            
            nc_l = cmin[pivot]
            
            while nc_l+cmax[nl-1-pivot] < nc:
                nc_l += 1
            
            solve(offset, pivot, nc_l)
            solve(pivot+offset+1, nl-1-pivot, nc-nc_l)
        
        if c > cmax[l] or c < cmin[l]:
            res.append(-1)
        else:
            solve(1, l, c)
        
        fptr.write(' '.join(map(str, res)))
        fptr.write('\n')
        
    fptr.close()
        
            
