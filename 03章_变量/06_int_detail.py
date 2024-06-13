# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :06_int_detail.py
# @Time     :2024/6/12 22:21
import sys

#int类型的细节
#在python中，int可以表示很大的数
n3 = 9 **888
print("n3 = ",n3,type(n3))

# python的整数有十进制，十六进制，八进制，二进制

# 十进制
print(10)

# 十六进制
print(0x10)

# 八进制
print(0o10)

# 二进制
print(0b10)

n1 = 0
n2 = 1
n3 = 2
n4 = 2 ** 15
n5 = 2 ** 30
n6 = 2 **128

# 在Python中字节数随着数字增大而增大（即：python的整型是变长的）
# 每次增量是四个字节

# 在Python中，可以通过sys.getsizeof 返回对象（数据）的大小，按照字节单位返回
print(sys.getsizeof(n1),"类型",type(n1))
print(sys.getsizeof(n2),"类型",type(n2))
print(sys.getsizeof(n3),"类型",type(n3))
print(sys.getsizeof(n4),"类型",type(n4))
print(sys.getsizeof(n5),"类型",type(n5))
print(sys.getsizeof(n6),"类型",type(n6))
