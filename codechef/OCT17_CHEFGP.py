# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/8 09:18


CHEFGP: 大厨和优秀的志愿者工作
题目描述
    大厨喜欢吃苹果，也喜欢吔蕉。这天，他来参加志愿工作，为有需求的人们免费发放水果。人
    们排成了一队，依次从大厨手里领水果。大厨会给每个人一种水果，要么香蕉要么苹果。
    大厨发放水果的信息以字符串 s 表示，字符串的每个字符是‘a’或‘b’，分别代表对应的人领到
    了苹果（apple）还是香蕉（banana）。
    工作结束后，大厨想知道自己做的怎么样。能让每个人都开心，对大厨而言是最好的奖赏。
    队伍中的每个人会暗中观察排在前面的人领导了什么。如果他发现他排在他前面的连续 K 个拿到
    的水果都和他自己的一样，那么他就会玻璃心。为了哄他开心，大厨只能自掏腰包，先送他一个
    昂贵的猕猴桃，再把原本要发给他的水果给他。大厨自然想要尽可能少花钱在猕猴桃上。
    注意，K 对于拿到苹果和香蕉的人来说是不同的。对于拿到苹果的人来说，K = x；对于拿
    到香蕉的人来说，K = y。
    请告诉大厨，他应该按什么顺序发放水果？

输入格式
    输入的第一行包含一个整数 T，代表测试数据的组数。接下来是 T 组数据。
    每组数据的第一行包含一个字符串 s，第二行包含两个整数 x 和 y。

输出格式
    对于每组数据，输出一个字符串，代表对大厨而言最优的发放水果的顺序。字符串中，以‘a’代
    表苹果、‘b’代表香蕉、‘*’代表猕猴桃。如果有多种答案，输出任意一种即可。请注意，输出的字
    符串中苹果和香蕉的数量应分别与输入中的数量相等。

数据范围和子任务
    • 1 ≤ T ≤ 50 • 1 ≤ |s| ≤ 105 • 1 ≤ x, y ≤ |s|
    子任务 1（20 分）：
        • x = y = 1
    子任务 2（30 分）：
        • 1 ≤ |s| ≤ 103
    子任务 3（50 分）：
        • 无附加限制

样例数据

输入
    5
    ab
    1 1
    aab
    1 1
    aabb
    1 2
    aaaaab
    2 1
    aaaa
    1 3

输出
    ab
    aba
    abba
    aa*abaa
    a*a*a*a

样例解释
    对于第一组数据，原本的顺序就已经能让每个人都开心了。
    对于第二组数据，排在第二个的人会因为前面一个人和他都拿到了苹果而不开心，因此可以
    交换他和后一人拿到的水果。
    对于第四组数据，不买猕猴桃没法让每个人开心。大厨可以买一个猕猴桃发给第三个人。这
    样前两个人拿到了苹果，第三个人先拿到了猕猴桃，又拿到了苹果，第四个人拿到了香蕉，后两
    个人拿到了苹果。这样一来所有人都开心了。


分析

按照x个a，y个b，x个a，y个b，...得到顺序可以满足要求， 如果a/x > b/y。

"""


def solve(a, b, x, y):
    ch = ['a', 'b']

    if a // x < b // y or (a // x == b // y and a % x == 0):
        a, b = b, a
        x, y = y, x
        ch = ['b', 'a']

    k = a // x
    xrem = a % x
    if xrem == 0:
        k -= 1
        xrem = x
    if k > 0:
        s = ''
        y1 = min(b // k, y)
        yrem = b - y1 * k
        for i in range(k):
            s += ch[0] * x
            if i < yrem and y1 < y:
                s += ch[1]
            s += ch[1] * y1
            if i >= yrem and y1 == 0:
                s += '*'
        s += ch[0] * xrem
        if y1 == y:
            s += ch[1] * yrem
        return s
    else:
        return ch[0] * x + ch[1] * y


T = int(input())
for ti in range(T):
    s = input()
    x, y = map(int, input().split())

    s = collections.Counter(s)

    print(solve(s['a'], s['b'], x, y))







