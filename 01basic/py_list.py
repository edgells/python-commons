

"""

    python list:
    1. 动态数组， 但由于内部存储的是 引用地址。 所以， 在同一个list内可以存储不同类型 item
    2. 自动扩容
    3. get o(1), pop(len(list)) and append() ==> o(1),  slice list[:n] o(len(list)-n))
    4. 分离式结构实现， list 属性声明 在一块mem area 并保存 data store 引用， data store 在另一个 area
"""

class A:
    pass


l1 = [1, "2"]
print(id(l1))
l1.append(A())

for n in range(1000):
    l1.append(n)
    print(id(l1))

    