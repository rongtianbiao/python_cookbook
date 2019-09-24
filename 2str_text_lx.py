# coding=utf-8

# 1.使用多个不同的字符分割字符串
import re
line = 'asdf fjdk; afed, fiek,asdf,   foo'
s_line = re.split(r'[,;\s]\s*', line)  # 分割符为逗号、封号、和空格
print(s_line)

# 2、检查字符串的开头和结尾
# 方法一匹配一种可能的开头： str.startswith()   str.endswith()
# 方法二： 匹配多种可能的开头和结尾，只需将匹配项放入到一个元组中，然后传给 str.startswith()   str.endswith()
filenames = ['makefile', 'fool.c', 'bar.py', 'spam.c', 'spam.h']
n_filenames = [file for file in filenames if file.endswith((".c", ".h"))]
print(n_filenames)


# 3、字符串搜索和替换
#  a、简单的替换用 str.replace(old, new)
#  b、复杂的用re.sub模块
text = "today is 11/27/2019. pycon starts 3/13/2019"
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', text))   # \3 \2 \2 是前面的捕获组号


# 4、删除字符串中不需要的字符
# a、strip()可以用于去掉开头或结尾的空白或指定字符
s = "sdfsfe//"
print(s.strip("//"))


# 5、字符串对其
# a、ljust()、 rjust()、 center()
text = "hello world"
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20, "="))
# b、format（）  注： format() 函数的一个好处是它不仅适用于字符串。它可以用来格式化任何值，使得它非常的通用。
text = 1.2232
print(format(text, ">30"))
print(format(text, "<30"))
print(format(text, "*^30"))  # 指定填充字符，将它写在对齐字符前面即可


# 6、合并拼接字符串
# a、合并的字符串是在一个序列或者 iterable 中，那么最快的方式就是使用 join() 方法
parts = ["is", "chicago", "not", "chicago"]
print(" ".join(parts))
# 注意：当我们使用加号 (+) 操作符去连接大量的字符串的时候是非常低效率的，因为加号连接会引起内存复制以及垃圾回收操作。
# 特别的，你永远都不应像下面这样写字符串连接代码：
s = ' '
for p in parts:
    s += p
# 一个相对比较聪明的技巧是利用生成器表达式
data = ["acme", 50, 91.1]
print(" ".join((str(i) for i in data)))
# b、当混合使用 I/O 操作和字符串连接操作的时候，有时候需要仔细研究你的程序,如：
# f. write(chunk1 + chunk2)

# f. write(chunk1)
# f. write(chunk2)
# 如果两个字符串很小，那么第一个版本性能会更好些，因为 I/O 系统调用天生就慢。另外一方面，如果两个字符串很大，那么第二个版本可能会更加高效，
# 因为它避免了创建一个很大的临时结果并且要复制大量的内存块数据。


# 7、字符串中插入变量
name = "tom"
age = 16
print("{:*>5} age is {:*<5}".format(name, age))


# 8、以指定列宽格式化字符串
import textwrap
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don' t look around the eyes, \
look into my eyes, you' re under. "
print(textwrap.fill(s, 40))

# textwrap 模块对于字符串打印是非常有用的，特别是当你希望输出自动匹配终端
# 大小的时候。你可以使用 os.get_terminal_size().columns 方法来获取终端的大小尺寸

# next: 数字日期和时间

