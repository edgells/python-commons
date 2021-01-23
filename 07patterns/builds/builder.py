"""
    建造者模式
    将一个复杂对象的构建与它的表示分离

    使得同样的构建过程可以创建不同的表示

"""


class PersonBuilder:

    def __init__(self, graphics, pen):
        self.graphics = graphics
        self.pen = pen

    def build_head(self):
        pass

    def build_body(self):
        pass

    def build_arm_left(self):
        pass

    def build_arm_right(self):
        pass

    def build_leg_left(self):
        pass

    def build_leg_right(self):
        pass


class PersonThinBuilder(PersonBuilder):
    def __init__(self):
        super(PersonThinBuilder, self).__init__("")