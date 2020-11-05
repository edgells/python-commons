"""
    python 中通过装饰器实现aop 编程

"""


def decorator(func):
    def wrap(*args, **kw):
        func(*args, **kw)

    return wrap
