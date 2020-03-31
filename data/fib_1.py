


"""
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

"""

fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)

def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)



"""
    台阶问题

"""

fib1 = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
# print(fib(89))
# print(fib(100))

def test(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return b

f = lambda n: 1 if n < 2 else f(n-1) * 2
print(f(10))



if __name__ == '__main__':
    print(test(89))