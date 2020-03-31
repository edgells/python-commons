


"""
    
    1. 引用计数
    最简单直接的办法， 对每个对象维护一个引用计数， 起始为1.

    缺点：
        维护引用计数消耗资源
        循环引用有内存泄漏
"""

class A:

    def __init__(self, b):
        self.a = 10
        self.b = b

class B:

    def __init__(self, a):
        self.b = 10
        self.a = a

