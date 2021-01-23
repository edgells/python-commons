"""
    策略模式
        定义一系列算法的方法， 从概念上讲， 所有这些算法完成的都是相同的工作。 只是实现不同而已。
        以相同得分方式调用所有的算法。减少各种算法与使用算法类之间的耦合

    封装变化
"""


class Strategy:

    def algorithm_method(self, money):
        """

        :return:
        """
        pass


class ConcreteStrategy(Strategy):

    def algorithm_method(self, money):
        print("算法 a 实现 %d" % money)


class ConcreteStrategyB(Strategy):

    def algorithm_method(self, money):
        print("算法 b 实现 %d" % money)


class Context:

    def __init__(self, strategy: str):
        self.strategy = self._create_strategy(strategy)

    @staticmethod
    def _create_strategy(strategy: str):
        """
        根据策略实例化算法
        :param strategy:
        :return:
        """
        if strategy == "正常收费":
            return ConcreteStrategy()

        elif strategy == "满 300 减 100":
            return ConcreteStrategyB()

    def context(self, money):
        """
        根据消费获取减免
        :param money:
        :return:
        """
        self.strategy.algorithm_method(money)


def test():
    context = Context("正常收费")
    context.context(100)


if __name__ == '__main__':
    test()
