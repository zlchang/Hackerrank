#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())
    maxint = sys.maxsize
    dist = [[maxint for _ in range(road_nodes)] for _ in range(road_nodes)]
    for i in range(road_edges):
        u = road_from[i]-1
        v = road_to[i]-1
        dist[u][v] = road_weight[i]
    for i in range(road_nodes):
        dist[i][i] = 0
    for k in range(road_nodes):
        for i in range(road_nodes):
            for j in range(road_nodes):
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])
        
        d = dist[x-1][y-1]
        if d == maxint:
            d = -1
        print(d)
