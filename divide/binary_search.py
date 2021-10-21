# -*- coding: utf-8 -*-

import algoruthm as ag


class Divide(ag.Algorithm):
    """分治算法实现二分搜索法"""

    def __init__(self, seq, target):
        super().__init__("分治法：二分搜索")
        self._seq = seq
        self._target = target

    def do(self):
        high = len(self._seq) - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if self._target == self._seq[mid]:
                return mid
            elif self._target > self._seq[mid]:
                low = mid + 1
            else:
                high = mid - 1


class DivideByRecursion(ag.Algorithm):
    """分治算法实现二分搜索法-递归实现"""

    def __init__(self, seq, target):
        super().__init__("分治法：二分搜索递归实现")
        self._seq = seq
        self._target = target

    def do(self):
        return self.rec(0, len(self._seq) - 1)

    def rec(self, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if self._target == self._seq[mid]:
            return mid
        elif self._target > self._seq[mid]:
            return self.rec(mid + 1, high)
        else:
            return self.rec(low, mid - 1)
