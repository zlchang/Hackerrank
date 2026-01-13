#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def getCost(g_nodes, g_edges, g_from, g_to, g_weight):
    # Print your answer within the function and return nothing
    n = g_nodes
    m = g_edges
    edges = [[] for i in range(n)]
    for i in range(m):
        u = g_from[i]-1
        v = g_to[i]-1
        w = g_weight[i]
        edges[u].append([v, w])
        edges[v].append([u, w])
    dist = [-1]*n
    
    pq = []
    
    heapq.heappush(pq, (0, 0))
    
    while pq:
        d, p = heapq.heappop(pq)
        if dist[p] > 0 and dist[p] < d:
            continue
        for e, w in edges[p]:
            c = w-dist[p]
            if c < 0:
                c = 0
            if dist[e] < 0 or c+dist[p] < dist[e]:
                dist[e] = c+dist[p]
                heapq.heappush(pq, (dist[e], e))
    
    if dist[n-1] < 0:
        return f'NO PATH EXISTS'
        
    return str(dist[n-1])
    
            
        

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    cost = getCost(g_nodes, g_edges, g_from, g_to, g_weight)
    
    sys.stdout.write(f'{cost}\n')
