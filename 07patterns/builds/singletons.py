"""
    单例模式， 在业务种经常会使用到。

"""


class Foo:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance

        cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance


f1 = Foo()
f2 = Foo()

print(id(f1))
print(id(f2))
