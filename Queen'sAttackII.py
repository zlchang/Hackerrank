#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    #column
    m1 = n-r_q+r_q-1
    #row
    m2 = n-c_q+c_q-1
    #pos diag
    m3 = min(n-r_q, n-c_q) + min(r_q-1, c_q-1) 
    #neg diag
    m4 = min(n-r_q, c_q-1) + min(r_q-1, n-c_q)
    al = 1-r_q-1
    au = n-r_q+1
    bl = 1-c_q-1
    bu = n-c_q+1
    cl = max(1-r_q, 1-c_q) - 1
    cu = min(n-r_q, n-c_q) + 1
    dl = max(1-r_q, -(n-c_q)) - 1
    du = min(n-r_q, -(1-c_q)) + 1
    for ob in obstacles:
        r_d = ob[0] - r_q
        c_d = ob[1] - c_q
        if c_d == 0:
            if r_d < 0:
                al = max(al, r_d)
            else:
                au = min(au, r_d)
        if r_d == 0:
            if c_d < 0:
                bl = max(bl, c_d)
            else:
                bu = min(bu, c_d)
        if r_d - c_d == 0:
            if r_d < 0:
                cl = max(cl, r_d)
            else:
                cu = min(cu, r_d)
        if r_d + c_d == 0:
            if c_d > 0:
                dl = max(dl, r_d)
            else:
                du = min(du, r_d)

        #print(r_d, c_d)
    return au-al+bu-bl+cu-cl+du-dl-8
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
