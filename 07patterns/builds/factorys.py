"""
    简单工厂模式
        创建一个关注实例化过程的类， 这个类就是工厂

    三个要素:
        一个基本的操作
        实现基本操作的类
        创建对象的类
"""


class Operation:

    def __init__(self, number_a=0, number_b=0):
        self.number_a = number_a
        self.number_b = number_b

    def get_result(self):
        """
            运算方法
        """
        pass


class OperationAdd(Operation):
    def get_result(self):
        """
            加法操作
        :return:
        """
        return self.number_a + self.number_a


class OperationSub(Operation):
    def get_result(self):
        """
            减法操作
        :return:
        """
        return self.number_a - self.number_b


class CreateOperation:
    @classmethod
    def create_operation(cls, operation: str):
        """
        负责具体操作的创建
        :param operation:
        :return:
        """
        if operation == "+":
            return OperationAdd()

        elif operation == "-":
            return OperationSub()


def test_operation():
    operation = CreateOperation.create_operation("+")
    operation.number_a = 10
    operation.number_b = 20
    print(operation.get_result())


if __name__ == '__main__':
    test_operation()
