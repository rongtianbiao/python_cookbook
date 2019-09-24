# coding=utf-8
# 1、数字的四舍五入
# a： 使用round(value, ndigits), 传给round()函数的ndigits参数可以是负数，这种情况会作用在十位、百位。。。
print(round(1.53, 1))
print(round(1.53232, 3))
print(round(153232, -3))


# 2、数字的格式化输出
# a：使用format()
x = 1234.56789
print(format(x, "0.2f"))
print(format(x, ">10.2f"))
print(format(x, "^10.2f"))
print(format(x, "*<20.2f"))
print(format(x, "0,.2f"))
# 使用指数计数法
print(format(x, "e"))
print(format(x, "0.3E"))


# 3、二八十六进制整数
# bin()、oct()、hex（）
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))
# 如果你不想输出0b、0o、0x的前缀的话，可以使用format()函数
print(format(x, "b"))
print(format(x, "o"))
print(format(x, "x"))
# 使用int将其它进制的整数转为10进制
print(int("34355", 8))

# 4、分数运算
# fractions模块可以被用来执行包含分数的数学运算
from fractions import Fraction
a = Fraction(3, 5)
b = Fraction(1, 5)
print(a + b)


# 5、大型数组运算
# 涉及到数组的重量级运算操作，可以使用 NumPy 库。 NumPy 的一个主要特征是它
# 会给 Python 提供一个数组对象，相比标准的 Python 列表而已更适合用来做数学运算。

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(type(ax))
print(np.full((2, 3), 5))

# next: 3.10







