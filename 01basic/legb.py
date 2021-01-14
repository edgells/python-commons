"""
    python 特有的作用域

"""


def foo():
    return [lambda y: x * y for x in range(1, 4)]


print([n(3) for n in foo()])
 