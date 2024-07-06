# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :08_bool_detail.py
# @Time     :2024/6/15 下午2:52
# 介绍
# 1、布尔类型也叫bool类型，取值True和False
# 2、True和False都是关键字，表示布尔值
# 3、bool类型适于逻辑运算，一般用于程序流程控制
# -条件控制语句
# -循环控制语句
# 比如判断某个条件是否成立，或者在某个条件满足时执行某些代码

# bool类型的基本使用
num1=100
num2=200
if num1 < num2:
    print("num1 > num2")

# 把num1 > num2的结果赋给result
result=num1 > num2
print("result=",result)

# 看result的数据类型
print("result的数据类型：",type(result))
print(type(1>-1))

# 使用细节
# 布尔类型只有两个值：True和False
# 在Python中，非0被视为真值，0被视为假值
# 布尔类型可以和其他数据类型进行比较，比如数字、字符串等
# Python会将 True视为 1，False 视为 0

b1=False
b2=True

print(b1+10) #?10
print(b2+10) #?11

if b1 == 0:
    print("OK")

if b2 == 1:
    print("Hi")

if 0:
    print("haha")

if -1:
    print("xixi")

if "lan":
    print("lan")