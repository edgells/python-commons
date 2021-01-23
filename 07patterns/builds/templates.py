"""
    模板方法模式
    定义一个操作中的算法的骨架, 而将特定步骤延迟到子类中, 模板方法是的子类不改变一个算法的结构
    就可以重定义该算法的某些特定步骤
"""


class TestPaper:
    def test_question_1(self):
        print("test question 1")

    def test_question_2(self):
        print("test question 2")

    def test_question_3(self):
        print("test question 3")


class StudentA(TestPaper):
    def test_question_1(self):
        super(StudentA, self).test_question_1()
        print("answer A")

    def test_question_2(self):
        super(StudentA, self).test_question_2()
        print("answer B")

    def test_question_3(self):
        super(StudentA, self).test_question_3()
        print("answer C")


class AbstractClass:
    def primitive_operation_1(self):
        pass

    def primitive_operation_2(self):
        pass

    def template_method(self):
        self.primitive_operation_1()
        self.primitive_operation_2()
        print("算法完成")
        print()


class ConcreteClassA(AbstractClass):
    def primitive_operation_1(self):
        print("具体类 A 方法 1 实现")

    def primitive_operation_2(self):
        print("具体类 A 方法 2 实现")


class ConcreteClassB(AbstractClass):
    def primitive_operation_1(self):
        print("具体类 B 方法 1 实现")

    def primitive_operation_2(self):
        print("具体类 B 方法 2 实现")


def test():
    conA = ConcreteClassA()
    conA.template_method()

    conB = ConcreteClassB()
    conB.template_method()


if __name__ == '__main__':
    test()
