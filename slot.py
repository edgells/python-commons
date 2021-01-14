"""
    当有很多小对象需要创建时, 应该考虑 slot

"""


class MyClass:

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


