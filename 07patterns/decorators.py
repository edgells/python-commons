"""
    装饰器moshi

"""


class Component:
    def operation(self, *args, **kwargs):
        pass


class ConcreteComponent(Component):
    def operation(self, *args, **kwargs):
        print("具体对象的操作")


class Decorator(Component):

    def __init__(self):
        self.component: Component = None

    def operation(self, *args, **kwargs):
        if self.component is not None:
            self.component.operation()

    def set_component(self, component: Component):
        self.component = component


class ConcreteDecoratorA(Decorator):

    def __init__(self):
        super(ConcreteDecoratorA, self).__init__()
        self.addedState = None

    def operation(self, *args, **kwargs):
        super(ConcreteDecoratorA, self).operation()
        self.addedState = "New state"
        print("具体装饰对象a的操作")


class ConcreteDecoratorB(Decorator):

    def operation(self, *args, **kwargs):
        super(ConcreteDecoratorB, self).operation()
        self.add_behavior()

    def add_behavior(self):
        print("add behavior")
