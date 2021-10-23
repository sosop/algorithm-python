# -*- coding: utf-8 -*-

from abc import abstractmethod
import time


class Algorithm(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def do(self):
        """具体算法具体实现"""
        pass


def compute_time(func):
    """
    计算方法或函数执行时间
    :param func:
    :return:
    """

    def wrapper(*args, **kw):
        local_time = time.time()
        func(*args, **kw)
        print(f'执行时长: {time.time() - local_time}')

    return wrapper
