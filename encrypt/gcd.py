# 最大公约数
def gcd(a, b):
    while a != 0:
        a, b = b % a, a

    return b


print(gcd(1203821039210, 123812030))

num = 0
for n in range(1, 100):
    num += n * n

print(num)
