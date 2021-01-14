


"""

    迭代器， 用来遍历集合容器的对象， 但是迭代器在执行的时候并不是在执行一个对象

    如果一个对象实现了, __getitem__或者 __iter__  哪么它就是一个可迭代的对象。

    而一个对象实现了, __next__ 方法. 哪么它就是迭代器. 为什么了, 因为在底层你可以看作, next在不断的调用 __getitem__ / __iter__
    example:
        for n in "hello world":
            print(n)

        注意这个地方的 for in 语法, 底层就是迭代器的写法. 会不断的调用 可迭代对象的 __next__ 方法得到对象


    而生成器也是一种迭代器, 但是由于所有数据由生成器在运行的时候动态生成, 也就是说白了, 空间换时间的方法减少内存消耗


    example:

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            yield b
            a, b =  b, a+b

"""

strs = "hello world"
# 对象的hash 调用， 会触发顶层对象的__hash__方法
# print(hash(strs))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    for n in fib(10):
        print(n)