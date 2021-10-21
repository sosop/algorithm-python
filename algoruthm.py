# -*- coding: utf-8 -*-

from abc import abstractmethod


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
