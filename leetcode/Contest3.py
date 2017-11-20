# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/9/24 09:55

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """

        N = len(S)
        s = [0] + [ord(v)-ord('a') for v in S]
        MAXN = 1010
        CSZ = 26

        nxt = [[0 for _ in range(CSZ)] for _ in range(MAXN)]
        lst = [[0 for _ in range(CSZ)] for _ in range(MAXN)]
        for i in range(CSZ):
            nxt[N+1][i] = N+1

        for i in range(N, 0, -1):
            for j in range(CSZ):
                nxt[i][j] = nxt[i+1][j]
            nxt[i][s[i]] = i

        for i in range(CSZ):
            lst[0][i] = 0

        for i in range(1, N+1):
            for j in range(CSZ):
                lst[i][j] = lst[i-1][j]
            lst[i][s[i]] = i

        dp = [[-1 for _ in range(MAXN)] for _ in range(MAXN)]
        MOD = 1000000007

        def dfs(l, r):
            ret = dp[l][r]
            if ret >= 0:
                return ret

            if l > r:
                return 1

            ret = 1
            for i in range(CSZ):
                a = nxt[l][i]
                b = lst[r][i]
                if a < b:
                    ret += dfs(a+1, b-1)
                if a <= r:
                    ret += 1

            ret %= MOD
            dp[l][r] = ret
            return ret

        ans = dfs(1, N)
        return MOD-1 if ans == 0 else ans-1




s = Solution()
print(s.countPalindromicSubsequences("bcccb"))
print(s.countPalindromicSubsequences("dda"))
print(s.countPalindromicSubsequences("bccb"))
print(s.countPalindromicSubsequences("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"))
