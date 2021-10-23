# -*- coding: utf-8 -*-

import algoruthm as ag
import random


class Merge(ag.Algorithm):
    def __init__(self):
        super().__init__('分治法-合并排序')
        self._r_list = list(range(1, 30))

    @ag.compute_time
    def do(self):
        random.shuffle(self._r_list)
        print("排序前：", self._r_list)
        self.merge_sort(0, len(self._r_list) - 1)
        print("排序后：", self._r_list)

    def merge(self, low, mid, high):
        i, j = low, mid + 1
        t_list = []
        while i <= mid and j <= high:
            if self._r_list[i] < self._r_list[j]:
                t_list.append(self._r_list[i])
                i += 1
            else:
                t_list.append(self._r_list[j])
                j += 1

        while i <= mid:
            t_list.append(self._r_list[i])
            i += 1
        while j <= high:
            t_list.append(self._r_list[j])
            j += 1
        k = 0
        for n in range(low, high + 1):
            self._r_list[n] = t_list[k]
            k += 1

    def merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)
