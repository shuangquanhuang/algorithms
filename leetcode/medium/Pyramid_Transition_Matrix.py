# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 4/1/18



We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
Example 2:
Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
Note:
bottom will be a string with length in range [2, 8].
allowed will have length in range [0, 200].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys


class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """

        A = collections.defaultdict(list)
        for x in allowed:
            A[x[0:2]].append(x[2])

        def dfs(row, index, top):
            # print(row, index, top)
            if len(row) == 1:
                return True

            if index >= len(row) - 1:
                return dfs(top, 0, "")

            block = row[index: index + 2]
            if block not in A:
                return False

            for b in A[block]:
                if dfs(row, index + 1, top + b):
                    return True

            return False

        return dfs(bottom, 0, "")


s = Solution()

print(s.pyramidTransition("ABC", ["ABD","BCE","DEF","FFF"]))
print(s.pyramidTransition("XXYX", ["XXX", "XXY", "XYX", "XYY", "YXZ"]))