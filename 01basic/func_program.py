from functools import reduce



result = reduce(lambda x ,y : x *y ,range(1 ,4))    # 阶乘
print(result)