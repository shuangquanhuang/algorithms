# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2020/8/5

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List
import math

INF = 10 ** 9 + 7
MAXN = 2000
MAXM = 10 ** 5

head = [-1 for _ in range(MAXN)]
pre = [-1 for _ in range(MAXN)]
dist = [-1 for _ in range(MAXN)]
inq = [-1 for _ in range(MAXN)]
incf = [-1 for _ in range(MAXN)]

cap = [0 for _ in range(MAXM)]
to = [0 for _ in range(MAXM)]
nxt = [0 for _ in range(MAXM)]
cost = [0 for _ in range(MAXM)]

tot = [1]


def draw(start, end):
    import networkx as nx
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('MacOSX')
    
    plt.figure('{}->{}'.format(start, end))
    g = nx.MultiDiGraph()
    
    for i in range(MAXN):
        inq[i] = False
    
    edge_labels = {}
    for u in range(start, end):
        i = head[u]
        while i > 0:
            v = to[i]
            if cap[i] > 0:
                g.add_edge(u, v)
                edge_labels[(u, v)] = '{}-{}'.format(cap[i] if cap[i] != INF else 'inf', cost[i])
            i = nxt[i]
    
    pos = nx.shell_layout(g)
    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_edge_labels(g, pos, edge_labels)
    plt.show()


def add_edge(u, v, w, c):
    tot[0] += 1
    i = tot[0]
    
    cap[i] = w
    to[i] = v
    cost[i] = c
    nxt[i] = head[u]
    head[u] = i


def add(u, v, w, c):
    add_edge(u, v, w, c)
    add_edge(v, u, 0, -c)


def spfa(start, end):
    for i in range(MAXN):
        dist[i] = -INF
        inq[i] = False
        incf[i] = 0
        pre[i] = -1
    
    q = collections.deque([start])
    inq[start] = True
    dist[start] = 0
    incf[start] = INF
    while q:
        u = q.popleft()
        inq[u] = False
        i = head[u]
        while i > 0:
            v = to[i]
            if cap[i] > 0 and dist[v] < dist[u] + cost[i]:
                dist[v] = dist[u] + cost[i]
                incf[v] = min(cap[i], incf[u])
                pre[v] = i
                if not inq[v]:
                    inq[v] = True
                    q.append(v)
            i = nxt[i]
    
    return dist[end] > 0


def max_flow_ek(start, end):
    ans = 0
    while spfa(start, end):
        u = end
        while u != start:
            cap[pre[u]] -= incf[end]
            cap[pre[u] ^ 1] += incf[end]
            u = to[pre[u] ^ 1]
        ans += dist[end] * incf[end]
    
    return ans


def distance(xa, ya, xb, yb):
    return int(math.floor(math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)))


if __name__ == '__main__':
    # sys.stdin = open('p3357.in', 'r')
    N, K = map(int, input().split())
    
    points = set()
    A = []
    for i in range(N):
        xa, ya, xb, yb = map(int, input().split())
        d = distance(xa, ya, xb, yb)
        xa <<= 1
        xb <<= 1
        if xa == xb:
            xb |= 1
        else:
            xa |= 1
        
        points.add(xa)
        points.add(xb)
        A.append((xa, xb, d))
    
    points = list(sorted(points))
    vi = {v: i + 1 for i, v in enumerate(points)}
    
    M = len(points)
    start, end = 0, M + 1
    
    add(start, 1, K, 0)
    for i in range(1, M):
        add(i, i + 1, INF, 0)
    
    for xa, xb, d in A:
        add(vi[xa], vi[xb], 1, d)
    
    add(M, end, INF, 0)
    
    # draw(start, end)
    print(max_flow_ek(start, end))