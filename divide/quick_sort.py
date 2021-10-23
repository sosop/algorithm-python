# -*- coding: utf-8 -*-

import algoruthm as ag
import random


class Quick(ag.Algorithm):

    def __init__(self):
        super().__init__("分治法-快速排序")
        self._r_list = list(range(1, 30))

    @ag.compute_time
    def do(self):
        random.shuffle(self._r_list)
        print("排序前：", self._r_list)
        self.quick_sort(0, len(self._r_list) - 1)
        print("排序后：", self._r_list)

    def quick_sort(self, low, high):
        if low < high:
            mid = self.compute_mid(low, high)
            self.quick_sort(low, mid - 1)
            self.quick_sort(mid + 1, high)

    def compute_mid(self, low, high):
        i, j = low, high
        pilot = self._r_list[low]

        while i < j:
            # 从右向左扫描
            while i < j and pilot < self._r_list[j]:
                j -= 1
            if i < j:
                self._r_list[i], self._r_list[j] = self._r_list[j], self._r_list[i]
            # 从左向右扫描
            while i < j and pilot >= self._r_list[i]:
                i += 1
            if i < j:
                self._r_list[i], self._r_list[j] = self._r_list[j], self._r_list[i]

        return i
