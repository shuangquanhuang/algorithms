# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/22 18:10

"""

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])

        def neighbors(r, c):
            return [(nr, nc) for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] if 0 <= nr < N and 0 <= nc < M]

        def hash(board):
            return '{}-{}-{}'.format(len(board), len(board[0]), ''.join([''.join(map(str, row)) for row in board]))

        id = 1
        shapes = set()
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    minr, maxr, minc, maxc = r, r, c, c
                    id += 1
                    grid[r][c] = id
                    q = [(r, c)]
                    while q:
                        x, y = q.pop()
                        for nr, nc in neighbors(x, y):
                            if grid[nr][nc] == 1:
                                grid[nr][nc] = id
                                q.append((nr, nc))
                                minr = min(minr, nr)
                                maxr = max(maxr, nr)
                                minc = min(minc, nc)
                                maxc = max(maxc, nc)
                    island = []
                    for x in range(minr, maxr+1):
                        row = [1 if grid[x][y] == id else 0 for y in range(minc, maxc+1)]
                        island.append(row)
                    shapes.add(hash(island))

        return len(shapes)

s = Solution()
print(s.numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
print(s.numDistinctIslands([[1,1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0],[1,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1],[0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,0],[1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,1,1,1],[1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1],[0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0],[0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0],[0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1],[0,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1],[0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1],[0,0,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,0],[1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1],[1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0],[1,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1],[0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0],[0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0],[1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0],[1,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,0,1],[0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0],[0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1,0,1,1,1],[0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0],[0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1],[1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0],[0,1,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,1],[1,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1],[0,0,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0],[1,1,0,0,1,1,0,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,1],[1,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0],[0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0],[0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0],[1,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,1],[0,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0,1],[0,1,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,1,1],[0,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,0,1,1],[0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,1],[1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1],[0,1,0,0,1,0,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0],[0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1],[0,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1],[1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1],[0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1],[1,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1],[0,0,1,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,1,1,0,1,1,0],[0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,1,0,1,1,1],[0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,0,0],[0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0],[1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,1,1],[0,1,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1],[1,0,1,0,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0],[0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0]]))