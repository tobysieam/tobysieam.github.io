# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :31_break_exercise01.py
# @Time     :2024/8/5 上午10:49

# 1-100以内的数求和，求出当和第一次大于20的当前控制循环的变量值是多少

"""
思路：
1、定义变量sum，累加和
2、使用for遍历1-100，大于20时，使用break退出
3、输出当前控制循环变量的值即可

"""

sum = 0

for i in range(1,101):
    sum += i
    if sum>20:
        break
print("i =",i)
