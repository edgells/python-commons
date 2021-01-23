"""
    appearance patterns
    外观模式
    为子系统中的一组接口提供一个一致的界面, 此模式定义了一个高层的接口

    什么时候使用外观模式:
        1. 一阶段:
            有意识将不同的两个层分离, 比如经典三层架构
            data access layer & business logic layer 建立 facade
            business logic layer & view layer 建立 facade
            这样就可以为复杂的子系统提供一个简单的接口. 而 在 spring boot 中 引入 service layer 不仅用于代码解耦, 也是便于扩展

        2. 二阶段:
            开发阶段, 子系统往往因为不断重构演化而变得复杂, 给外部客户端调用造成困难. 增加一个 facade 可以提供一个简单的接口减少它们之间的依赖

        3. 三阶段:
            在维护大型的系统时, 可能这个系统已经非常难维护, 但因为它包含非常重要的功能, 新功能必须依赖它, 这时就可以为旧系统设计 facade 便于新功能实现

"""


class SubSystem:
    def method_one(self):
        print("子系统方法一")


class SubSystemTwo:
    def method_one(self):
        print("子系统方法二")


class Facade:

    def __init__(self):
        self.one = SubSystem()
        self.two = SubSystemTwo()

    def method_a(self):
        self.one.method_one()
        self.two.method_one()

    def method_b(self):
        self.two.method_one()


def test():
    facade = Facade()
    facade.method_a()
    facade.method_b()


if __name__ == '__main__':
    test()
