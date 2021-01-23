"""
    proxy patterns: 代理模式
    为其它对象提供一种代理以控制对这个对象的操作

    要素：
        一个开放的方法集(interface)
        实现相应方法集的proxy 对象
        实现了相应方法集的类


    应用：
        远程代理, 为一个对象在不同地址空间提供局部代表， 这样就可以隐藏一个对象存在于不同地址空间的事实
            哪么两个进程间， 是否可以通过这样的方式实现数据共享

        虚拟代理, 根据需要创建开销很大的对象, 通过它存放实例化需要很长时间的真实对象

        安全代理, 用来控制真实对象访问时的权限
"""


class GiveGift:
    def give_dolls(self):
        raise NotImplemented("give dolls not implementation")

    def give_flowers(self):
        raise NotImplemented("give flowers not implementation")

    def give_give_chocolate(self):
        raise NotImplemented("give chocolate not implementation")


class Pursuit(GiveGift):

    def __init__(self, mm):
        self.mm = mm

    def give_dolls(self):
        print(self.mm, "\t 送你娃娃")

    def give_flowers(self):
        print(self.mm, "\t 送你鲜花")

    def give_give_chocolate(self):
        print(self.mm, "\t 送你巧克力")


class Proxy(GiveGift):

    def __init__(self, mm):
        self.gg = Pursuit(mm)

    def give_dolls(self):
        self.gg.give_dolls()

    def give_flowers(self):
        self.gg.give_flowers()

    def give_give_chocolate(self):
        self.gg.give_give_chocolate()


def test():
    mm = "娇娇"

    print("hello" + "world")
    proxy = Proxy(mm)

    proxy.give_dolls()
    proxy.give_flowers()
    proxy.give_give_chocolate()


if __name__ == '__main__':
    test()
