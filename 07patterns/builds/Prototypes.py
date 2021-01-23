"""
    如果需要根据现有对象复制出新对象， 并对其做一定的修改， 哪么我们可以使用原型模式

    潜复制:

"""
import copy
import sys


class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_objects(Class, *args, **kwargs):
    return Class(*args, **kwargs)


prototype1 = Point(1, 2)
prototype2 = eval("{}({}, {})".format("Point", 2, 4))
prototype3 = getattr(sys.modules[__name__], "Point")(3, 6)
prototype4 = globals()["Point"](4, 8)
prototype5 = make_objects(Point, 4, 5)

# 通过clone 对象， 的确可以实现原型模式， 但是第7种方法更加python
prototype6 = copy.deepcopy(prototype5)
prototype6.x = 6
prototype6.y = 12

prototype7 = prototype1.__class__(7, 14)
