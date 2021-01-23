"""
    工厂方法
        定义一个用于创建对象的接口, 让子类决定实例化哪一个类, 工厂方法使一个类的实例化延迟
        到其子类
"""


class Factory:
    def create_factory(self):
        pass


class Less:
    def sweep(self):
        print("扫地")


class Undergraduate(Less):
    pass


class UndergraduateFactory(Factory):

    def create_factory(self):
        return Undergraduate()
