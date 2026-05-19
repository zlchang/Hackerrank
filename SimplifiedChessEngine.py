#!/bin/python3

import os
import sys

#
# Complete the simplifiedChessEngine function below.
#
def kmoves(k, mw, mb):
    n = 4
    i = k//n
    j = k%4
    mvs = []
    for d in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        for s in [(1, 2), (2,1)]:
            x = i + d[0]*s[0]
            y = j + d[1]*s[1]
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            nk = x*n+y
            if nk in mw:
                continue
            mvs.append(nk)
    return mvs
def bmoves(k, mw, mb):
    n = 4
    i = k//n
    j = k%4
    mvs = []
    for d in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        for s in range(1, n):
            x = i+d[0]*s
            y = j+d[1]*s
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            nk = x*n+y
            if nk in mw:
                break
            mvs.append(nk)   
            if nk in mb:
                break
    return mvs
def rmoves(k, mw, mb):
    n = 4
    i = k//n
    j = k%4
    mvs = list()
    #print(mw)
    #print(mb)
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        for s in range(1, n):
            x = i+d[0]*s
            y = j+d[1]*s
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            nk = x*n+y
            #print(nk)
            if nk in mw:
                #print('{} in white'.format(nk))
                break
            mvs.append(nk)   
            if nk in mb:
                break
    #print(mvs)
    return mvs
def qmoves(k, mw, mb):
    return rmoves(k, mw, mb) + bmoves(k, mw, mb)
def code(mc):
    rc = 0
    rr = [] 
    rn = []
    rb = []
    for k, p in mc.items():
        i = k+1
        if p == 'Q':
            rc |= i
        elif p == 'N':
            rn.append(i)
        elif p == 'B':
            rb.append(i)
        elif p == 'R':
            rr.append(i)
    if len(rr) == 1:
        rc |= rr[0] << 14
    elif len(rr) == 2:
        if rr[0] < rr[1]:
            rc = rc | (rr[0] << 19) | (rr[1] << 14)
        else:
            rc = rc | (rr[1] << 19) | (rr[0] << 14)
    if len(rb) == 2:
        if rb[0] < rb[1]:
            rc = rc | (rb[0] << 9) | (rb[1] << 4)
        else:
            rc = rc | (rb[1] << 9) | (rb[0] << 4)
    elif len(rn) == 2:
        if rn[0] < rn[1]:
            rc = rc | (rn[0] << 9) | (rn[1] << 4)
        else:
            rc = rc | (rn[1] << 9) | (rn[0] << 4)
    else:
        for ri in rn:
            rc |= ri << 4
        for ri in rb:
            rc |= ri << 9
    return rc
            
def simplifiedChessEngine(whites, blacks, moves):
    #
    # Write your code here.
    #
    n = 4
    bw = {} 
    for p,c,r in whites:
        x = ord(r) - ord('1')
        y = ord(c) - ord('A')
        k = n*x + y
        bw[k] = p
    bb = {}
    for p,c,r in blacks:
        x = ord(r) - ord('1')
        y = ord(c) - ord('A')
        k = n*x + y
        bb[k] = p
    #print(bw, bb)
    memo = {}
    def solve(mw, mb, cntr):
        cw = code(mw)
        cb = code(mb)
        tag = (cw, cb, cntr)
        if cntr == moves and moves % 2 == 0:
            memo[tag] = False
            return False
        if 'Q' not in mw.values():
            memo[tag] = False
            return False
        if cntr == moves:
            memo[tag] = True
            return True
        if tag in memo:
            return memo[tag]
        #if cntr == 2:
            #print(mb)
            #print(mw)
            #print('cntr={}'.format(cntr))
        flag = False
        
        for kk, vv in mw.items():
            nmv = []
            if vv == 'Q':
                nmv = qmoves(kk, mw, mb)
            elif vv == 'N':
                nmv = kmoves(kk, mw, mb)
            elif vv == 'B':
                nmv = bmoves(kk, mw, mb)
            elif vv == 'R':
                nmv = rmoves(kk, mw, mb)
            #if (kk == 14 and vv == 'B') or cntr == 1:
                #print(kk, vv)
                #print(nmv)
            for ss in nmv:
                #print(ss)
                cmw = mw.copy()
                cmw.pop(kk) 
                cmw[ss] = vv
                bp = vv
                fb = ss in mb
                if fb:
                    bp = mb.pop(ss)
                    #if cntr == 1:
                        #print('{} fount black at {} bp={}'.format(cntr, ss,bp))
                cntr += 1
                st = solve(mb, cmw, cntr)
                cntr -= 1           
                if fb:
                    mb[ss] = bp
                    #if cntr == 1:
                        #print('add black at {} bp={}'.format(ss,bp))
        
                #if cntr == 2:
                    #print(f'white: {cntr}, {st}, {vv}, {ss} from {kk}')
                if st == False:
                    memo[tag] = True
                    return True                  
        return flag
    res = solve(bw, bb, 0)
    if res:
        return 'YES'
    return 'NO'        
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        wbm = input().split()

        w = int(wbm[0])

        b = int(wbm[1])

        m = int(wbm[2])

        whites = []

        for _ in range(w):
            whites.append(list(map(lambda x: x[0], input().rstrip().split())))

        blacks = []

        for _ in range(b):
            blacks.append(list(map(lambda x: x[0], input().rstrip().split())))
        if g_itr == 54:
            print(whites)
            print(blacks)
            print(m)
        result = simplifiedChessEngine(whites, blacks, m)
        fptr.write(result+'\n')

    fptr.close()
