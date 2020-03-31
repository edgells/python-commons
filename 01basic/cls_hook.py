


class Foo:

    _instance = None

    def __new__(cls, *args, **kwargs):

        if cls._instance == None:
            object.__init__(Foo)

        return cls._instance


class Foo2(Foo):

    def __init__(self):

        self.a = 10
        self.b = 10

print(id(Foo()))
print(id(Foo2()))


#----------------------------------------
class A:
    def __init__(self):
        pass


class B(A):
    def __init__(self):
        super().__init__()


print(id(A()))
print(id(B()))