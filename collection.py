"""
    python collection 使用

"""

from collections import namedtuple, defaultdict, deque, OrderedDict, Counter

colors = (
    ('Yasoob', 'Yellow'),
    ('Ali', "blue"),
    ("Arham", "green"),
)

fav = defaultdict(list)

for name, color in colors:
    fav[name].append(color)

print(fav)

# nametuple 使用 尤其在数据库映射上面很有用
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p._asdict())  # k -> v
print(Point._make([30, 30]))  # 从序列创建一个对象


d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
print(''.join(d.keys()))

# 常用计数器
print(Counter([name for name, color in colors]))

# 统计行数
with open('iters.py', 'r', encoding='utf-8') as f:
    lines = Counter(f)
print(lines)


# 双端队列
d = deque(maxlen=30)    # 超过最大尺寸将会从另一端被寄出去

d.append('1')
d.append('3')
d.append('8')
d.append('11')
d.pop()
d.popleft()


#




print(d)