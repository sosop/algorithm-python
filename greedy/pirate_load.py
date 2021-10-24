# -*- coding: utf-8 -*-

import algoruthm as ag
import random
import divide.quick_sort as dqs


class Pirate(ag.Algorithm):

    def __init__(self):
        super().__init__("贪心算法-最优装载问题")
        self._treasure = list(range(3, 29))
        self._trunk = 19

    def do(self):
        print("各宝物的重量排序：", self._treasure)
        print(f"此卡车能存储{self.decide_by_weight()}个货物")

    def decide_by_weight(self):
        num = 0
        t_weights = 0
        for weight in self._treasure:
            t_weights += weight
            if t_weights > self._trunk:
                return num
            num += 1
        return -1
