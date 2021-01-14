
"""

    python 自省
"""

# dir 可以获取给定对象的属性和方法
my_list = list(range(10))
print(dir(my_list))
print(dir())

a = 10
b = 20

# 获取对象不同的唯一id值
print(id(a))
print(id(b))

# 用来获取对象类型
print(type(my_list))


# inspect
import inspect
print(inspect.getmembers(str))
