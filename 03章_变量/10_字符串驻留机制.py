# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :10_字符串驻留机制.py
# @Time     :2024/6/16 上午10:37
import sys

# 讲解字符串驻留机制

str1 = "Hello"
str2 = "Hello"
str3 = "Hello"

# id()函数是，可以返回对象/数据的内存地址
print("str1的地址是:",id(str1))
print("str2的地址是:",id(str2))
print("str3的地址是:",id(str3))


# 驻留机制几种情况讨论（注意：需要在交互模式下 win+r->python）
# (1)、字符串是由26个英文字母大小写，0-9，_组成
# (2)、字符串长度为 0 或 1 时
# (3)、字符串在编译时进行驻留，而非运行时
# (4)、[-5,256]的整数数字

# 遍历时驻留，而非运行
a = "abc"
b="".join(["a","bc"])

# sys中的intern方法可以强制2个字符串指向同一个对象
S1 = "abc#"
S2 = "abc#"
S2 = sys.intern(S1)

# pycharm对字符串进行了优化处理
str1 = "abc123#"
str2 = "abc123#"
print(id(str1),id(str2))

# 字符串驻留机制的好处
# 当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁的创建和销毁，提升效率和节约内存
