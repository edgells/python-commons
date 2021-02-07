import time

"""
    yield 和 yield from 后面一样也不能跟阻塞调用
"""


def test():
    while 1:
        item = (yield from time.sleep(10))
        print(item)


corou = test()

next(corou)
while 1:
    time.sleep(1)
    corou.send("hello")
