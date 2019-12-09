# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/3/19

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


class MyCircularDeque:
    
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.data = [0] * (k+1)
        self.start = 0
        self.end = 1
        self.length = 0
        self.capacity = k
    
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.length >= self.capacity:
            return False
        
        self.length += 1
        self.data[self.start] = value
        self.start = (self.capacity + self.start - 1) % self.capacity
        return True
        
    
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.length >= self.capacity:
            return False
        
        self.length += 1
        self.data[self.end] = value
        self.end = (self.end + 1) % self.capacity
        
        return True
        
    
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        
        if self.length <= 0:
            return False
        
        self.length -= 1
        self.start = (self.start + 1) % self.capacity
        
        return True
        
    
    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        
        if self.length <= 0:
            return False
        
        self.length -= 1
        self.end = (self.end - 1) % self.capacity
        
        return True
        
    
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.length <= 0:
            return -1
        
        return -1 if self.length <= 0 else self.data[(self.start + 1) % self.capacity]
        
    
    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        
        return -1 if self.length <= 0 else self.data[(self.end - 1) % self.capacity]
    
    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        
        return self.length <= 0
    
    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        
        return self.length >= self.capacity

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# ["MyCircularDeque",]
# [[3],]

["MyCircularDeque",]



d = MyCircularDeque(4)
for op, val in zip(["MyCircularDeque","insertFront","deleteLast","getFront","insertLast","insertFront","getFront","getRear","getFront","getFront","getRear","insertLast"],
                   [[2],[7],[],[],[5],[0],[],[],[],[],[],[0]]):
    if op == 'MyCircularDeque':
        d = MyCircularDeque(val[0])
    elif op == 'insertLast':
        print(d.insertLast(val[0]))
    elif op == 'insertFront':
        print(d.insertFront(val[0]))
    elif op == 'getRear':
        print(d.getRear())
    elif op == 'isFull':
        print(d.isFull())
    elif op == 'deleteLast':
        print(d.deleteLast())
    elif op == 'getFront':
        print(d.getFront())
    elif op == 'deleteFront':
        print(d.deleteFront())
    # print(d.data)
    
    # [null,true,true,-1,true,true,0,5,0,0,5,false]