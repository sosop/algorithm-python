# -*- coding: utf-8 -*-

import sys
import getopt
import divide.binary_search as dbs
import divide.merge_sort as dms
import divide.quick_sort as dqs
import random
import greedy.pirate_load as gpl

if __name__ == "__main__":

    tips = '''执行:python run.py [算法大类 算法实现]
    
    分治算法: python run.py -d [0-3]
             0: 二分搜索
             1: 二分搜索递归实现
             2: 归（合）并排序
             3: 快速排序
    贪心算法: python run.py -g [0-9]
             0: 最优装载
    '''

    argv = sys.argv[1:]

    if len(argv) == 0:
        print(tips)
        exit(0)

    try:
        opts, args = getopt.getopt(argv, "hd:g:", ["help", "divide", "greedy"])
    except Exception as e:
        print(tips)
        exit(-1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(tips)
            exit(0)
        if opt in ('-d', '--divide'):
            if arg in ['0', '1']:
                seq = [6, 9, 14, 16, 19, 22, 23, 29, 33, 39]
                print("有序数列为：", seq)
                s = random.choice(seq)
            if arg == '0':
                al = dbs.Divide(seq, s)
                print(al.name, " ", s, '的下标索引为：', al.do())
            if arg == '1':
                al = dbs.DivideByRecursion(seq, s)
                print(al.name, " ", s, '的下标索引为：', al.do())
            if arg == '2':
                al = dms.Merge()
                al.do()
            if arg == '3':
                al = dqs.Quick()
                al.do()
        if opt in ('-g', '--greedy'):
            if arg == '0':
                al = gpl.Pirate()
                al.do()

