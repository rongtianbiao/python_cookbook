# coding=utf-8
# 1、对字典的key进行排序
prices = {
    "acme": 45.34,
    "aapl": 612.78,
    "ibm": 205.55,
    "hpq": 37.22,
    "fb": 10.75
}

sort_l = sorted(prices, key=lambda k: prices[k])
print(sort_l)


# 2、查找字典中相同的key或value或items
a = {"x": 1, "y": 2, "z": 3}
b = {"w": 10, "x": 11, "y": 2}
# 利用集合的交和与
print(set(a.keys()) & set(b.keys()))
print(set(a.keys()) - set((b.keys())))
print(set(a.items()) & set(b.items()))
print(set(a.keys()) | set(b.keys()))


# 3、利用集合相差排除字典中不需要的几个key重新生成字典
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# 去掉b、 e
new_d = {k: d[k] for k in set(d.keys()) - {"d", "e"}}
print(new_d)


# 4、命名切片
s = "3457668980-0-jjjjjjj"
print(s[slice(4, 9)])


# 5、找出序列中出现次数最多的元素
from collections import Counter
l = [1, 334, 45, 4, 4, 4, 5, 5, 6, 6, 789, 5466, 78, 0]
l_count = Counter(l)
print(l_count)
# 用most_common查出出现最高数字
print(l_count.most_common(3))
# Count对象可以进行数学运算
l1 = [1, 334, 45, 4, 4, 4, 6, 789, 5466, 78, 0]
l1_count = Counter(l1)
print(l1_count)
print(l_count + l1_count)


# 6、通过一个或几个关键字对字典列表进行排序
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# 方法一用lamdba函数(慢)
l_rows = sorted(rows, key=lambda x: x["uid"])
print(l_rows)
# 方法二用itemgetter（快）
from operator import itemgetter
i_rows = sorted(rows, key=itemgetter("uid", "lname"))
print(i_rows)


# 7、多值字典
# 利用多值字典将相同的日期的数据进行分组
rows = [
    {' address': ' 5412 N CLARK', ' date': ' 07/01/2012'},
    {' address': ' 5148 N CLARK', ' date': ' 07/04/2012'},
    {' address': ' 5800 E 58TH', ' date': ' 07/02/2012'},
    {' address': ' 2122 N CLARK', ' date': ' 07/03/2012'},
    {' address': ' 5645 N RAVENSWOOD', ' date': ' 07/02/2012'},
    {' address': ' 1060 W ADDISON', ' date': ' 07/02/2012'},
    {' address': ' 4801 N BROADWAY', ' date': ' 07/01/2012'},
    {' address': ' 1039 W GRANVILLE', ' date': ' 07/04/2012'},
]
from collections import defaultdict
rows_by_date = defaultdict(list)   # 构建一个多值字典
for row in rows:
    rows_by_date[row[" date"]].append(row)
print(rows_by_date)


# 8、过滤序列元素
# 最简单的过滤列表元素是用列表推导式和生成器表达式
my_list = [1, 3, 5, -5, -3, -7, 23, -4]
print([n for n in my_list if n > 0])
print((n for n in my_list if n > 0))   # 生成器占用内存少
# 使用高阶函数filter
print(filter(lambda x: 1 if x > 0 else 0, my_list))


# 9、从字典中提取子集
prices = {
    "acme": 45.34,
    "aapl": 612.78,
    "ibm": 205.55,
    "hpq": 37.22,
    "fb": 10.75
}
new_prices = {k: v for k, v in prices.items() if v > 100}
print(new_prices)


# 10、合并字典
a = {"x": 2, "y": 3}
b = {"y": 4, "z": 5}
a.update(b)
print(a)













