# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/19 21:53


如果所有数的最大公约数不在集合中，返回-1。

gcd(x, y) <= min(x, y)，这个公约数是集合中的最小的数字

否则在每个数字前面加上这个数字即可。

"""

N = int(input())
A = [int(x) for x in input().split()]

def gcd(x, y):
    if x < y:
        return gcd(y, x)
    if y == 0:
        return x

    return gcd(y, x%y)

x = A[0]
for v in A[1:]:
    x = gcd(x, v)

if A[0] != x:
    print(-1)
else:
    print(2*len(A)-1)
    print((" %d " % A[0]).join(map(str, A)))

