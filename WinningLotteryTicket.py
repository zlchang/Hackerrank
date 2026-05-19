#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'winningLotteryTicket' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY tickets as parameter.
#

def winningLotteryTicket(tickets):
    # Write your code here
    n = len(tickets)
    m = 1 << 10
    freq = [0]*m
    
    for t in tickets:
        p = 0
        for s in t:
            i = ord(s) - ord('0')
            p = p | (1 << i)
        freq[p] += 1
    res = 0
    for i in range(m):
        fi = freq[i]
        if i == m-1:
            res += fi*(fi-1)//2
        for j in range(i+1, m):
            fj = freq[j]
            if i | j == m-1:
                res += fi*fj
    return res
        
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()
