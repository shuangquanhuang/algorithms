# -*- coding: utf-8 -*-

"""
created by huash06 at 2015-07-16 15:53

嘟嘟最近发明了一种新的随机数生成器，这个随机数生成器可以随机等概率的生成1到n之间的数。烦人的慢慢提出了一些问题，需要嘟嘟解决，问题分为两种：

0 n m: 求可以产生 1 到 n 的随机数生成器，需要生成随机数次数的期望，使得最后生成的 m 个数是相同的。

1 n m: 求可以产生 1 到 n 的随机数生成器，需要生成随机数次数的期望，使得最后生成的 m 个数两两之间互不相同。

输入格式

输入包含多组测试数据，对于每组测试数据：

第一行包含一个整数T ( 1 ≤ T ≤ 100)，表示慢慢提出询问的次数。

接下来T行每行包含三个整数，表示一次询问，其中1 ≤ n, m ≤ 10^{6}10
​6
​​ 。

输入保证所有的第二种操作 n ≥ m。

为了避免浮点误差，输入保证所有输入数据对应的结果不超过 10^{9}10
​9
​​ 。

输出格式

对于每组测试数据的每次询问，输出一个小数，保留三位小数。

样例输入

3
0 2 3
1 5 3
1 6 1
样例输出

7.000
4.333
1.000
"""
__author__ = 'huash06'

import datetime
import sys
import math
import collections

T = int(raw_input())

for ti in range(T):
    K, N, M = map(int, raw_input())
    print K, N, M

math.log()


