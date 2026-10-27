#!/bin/python3

import math
import os
import random
import re
from collections import defaultdict
from collections import deque
import sys


def dfs(start, graph, pre, post, counter):
    pre[start] = counter[0]
    counter[0] += 1
    for ch in graph[start]:
        dfs(ch, graph, pre, post, counter)
    post[start] = counter[0]
def update(index, val, nindex, fenwick):
    while index < nindex:
        fenwick[index] += val
        index += index & (-index)
def query(index, fenwick):
    qsum = 0
    while index > 0:
        qsum += fenwick[index]
        index -= index & (-index)
    return qsum
if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))
                        
    s = int(input().strip())

    strands = [str() for _ in range(s)]
    sfirst = [list() for _ in range(n)]
    slast = [list() for _ in range(n)]
 
    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        
        strands[s_itr] = d
        if first > 0:
            sfirst[first-1].append(s_itr)
        slast[last].append(s_itr)
    
    trie = [defaultdict(int)] #defaultdict(int) for _ in range(mnodes)]
    output = [0 for _ in range(n)]
    node = 0
    for gi, g in enumerate(genes):
        current = 0
        for l in g:
            if l not in trie[current]:
                trie[current][l] = node+1
                trie.append(defaultdict(int))
                node += 1
            current = trie[current][l]
        output[gi] = current
    #print(output)
    #print(node)
    fail = [0 for _ in range(node+1)]
    tree = [ list() for _ in range(node+1)]

    qq = deque()
    qq.append(0)
    
    while qq:
        state = qq.popleft()
        #if output[suffix]:
            #output[state].update(output[suffix])
        for l in trie[state]:
            suffix = fail[state]
            child = trie[state][l]
            if state == 0:
                fail[child] = 0
            else:
                while l not in trie[suffix] and suffix > 0:
                    suffix = fail[suffix]
                if l in trie[suffix]:
                    fail[child] = trie[suffix][l]
                else:
                    fail[child] = 0
            fchild = fail[child]
            tree[fchild].append(child)
            qq.append(child)
    #print(output)
    #print(fail)
    snodes = [[] for _ in range(s)]
    for gi, g in enumerate(strands):
        current = 0
        for l in g:
            while current > 0 and l not in trie[current]:
                current = fail[current]
            if l in trie[current]:
                snodes[gi].append(trie[current][l])
                current = trie[current][l]
    #print(snodes)
                

    trie.clear()
    fail.clear()
    
    hstart = [0 for _ in range(node+1)]
    hend = [0 for _ in range(node+1)]
    cntr = [0]
    dfs(0, tree, hstart, hend, cntr)
    node = cntr[0]
    if 0: 
        stack = [0]
        visited = list()
        node = 0
        while stack:
            state = stack[-1]
            if visited and state == visited[-1]:
                hend[state] = node
                visited.pop()
                stack.pop()
            else:
                hstart[state] = node
                node += 1
                visited.append(state)
                for child in tree[state]:
                    stack.append(child)
    #print(node)
    #print(hstart[:node])
    #print(hend[:node])
    tree.clear()
    
    fenwick = [0 for _ in range(node)]
    results = [0 for _ in range(s)]   
    for n_itr in range(n):
        onode = output[n_itr]
        hh = health[n_itr]
        update(hstart[onode], hh, node, fenwick)
        update(hend[onode], -hh, node, fenwick)
        for q_itr in sfirst[n_itr]:
            for qnode in snodes[q_itr]:
                results[q_itr] -= query(hstart[qnode], fenwick)
        for q_itr in slast[n_itr]:
            for qnode in snodes[q_itr]:
                results[q_itr] += query(hstart[qnode], fenwick)
   
    #print(strands)
    a = min(results)
    b = max(results)
    print(a, b)
