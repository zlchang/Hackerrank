#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aOrB' function below.
#
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING a
#  3. STRING b
#  4. STRING c
#

def aOrB(k, a, b, c):
    # Write your code here
    na = a.bit_length()
    nb = b.bit_length()
    nc = c.bit_length()   
    nm = max(na, nb, nc)
    #print(nm)
    cntr = 0
    sa = format(a, 'b')
    ap = [0]*nm
    for i in range(nm):
        if i > nm-na-1:
            ap[i] = int(sa[i-nm+na])
    #print(sa)
    #print(ap)
    bp = [0]*nm
    sb = format(b, 'b')
    for i in range(nm):
        if i > nm-nb-1:
            bp[i] = int(sb[i-nm+nb])
    #print(sb)
    #print(bp)
    sc = format(c, 'b')
    
    for i in range(nm):
        ai = 0
        if i > nm-na-1:
            ai = int(sa[i-nm+na])
        bi = 0
        if i > nm-nb-1:
            bi = int(sb[i-nm+nb])
        ci = 0
        if i > nm-nc-1:
            ci = int(sc[i-nm+nc])
        if ai | bi == 0 and ci == 1:
            bp[i] = 1
            cntr += 1
        elif ai | bi == 1 and ci == 0:
            if ai == 0:
                bp[i] = 0
                cntr += 1
            elif bi == 0:
                ap[i] = 0
                cntr += 1
            else:
                ap[i] = 0
                bp[i] = 0
                cntr += 2
    #print(ap)
    #print(bp)
    #print('cntr={}'.format(cntr))
    if cntr > k:
        return ['-1']
   
    for i in range(nm):
        ci = 0
        if i > nm-nc-1:
            ci = int(sc[i-nm+nc])
        if ci == 1 and ap[i] == 1 and bp[i] == 1 and cntr < k:
            ap[i] = 0
            cntr += 1
        elif ci == 1 and ap[i] == 1 and bp[i] == 0 and cntr+1 < k:
            ap[i] = 0
            bp[i] = 1
            cntr += 2
         
    sap = ''.join(map(str, ap))
    #print(sap)
    sbp = ''.join(map(str, bp))
    #print(sbp)
    return ['{:X}'.format(int(sap, 2)), '{:X}'.format(int(sbp, 2))]

if __name__ == '__main__':
    q = int(input().strip())
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for q_itr in range(q):
        k = int(input().strip())

        a = int(input(), 16)

        b = int(input(), 16)

        c = int(input(), 16)

        result = aOrB(k, a, b, c)
        fptr.write('\n'.join(result))
        fptr.write('\n')
    fptr.close()
