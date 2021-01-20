"""

    抽象工厂用来创建复杂对象

    这种对象由许多小对象组成， 而这些小对象都属于某个特定的系列

"""


class DiagramFactory:

    def make_diagram(self, width, height):
        return Diagram(width, height)

    def make_rectang(self, x, y, width, height, fill='white', stroke="black"):
        return Rectang(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return Text(x, y, text, fontsize)


"""
    如果子类某个方法要根据情况来决定用什么类去实例化相关对象， 哪么可以考虑工厂方法
    
"""
