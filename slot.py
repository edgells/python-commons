"""
    当有很多小对象需要创建时, 应该考虑 slot

"""


class MyClass:
    __slots__ = ('name', 'identifier')

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
