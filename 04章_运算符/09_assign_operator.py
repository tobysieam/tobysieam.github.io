# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :09_assign_operator.py
# @Time     :2024/7/6 下午9:42

num = 10
i = 100
i+=100
print("i=",i)
i-=100
print("i=",i)
i*=2
print("i=",i)

a=10
b=20
# 有两个变量a和b，要求将其交换
print(f"没有交换前 a={a},b={b}")
temp = a
a = b
b = temp
print(f"交换 a={a},b={b}")
'''
python支持用一种简单的方式实现变量交换
x,y = y,x
'''
print(f"没有交换前 a={a},b={b}")
a,b = b,a
print(f"交换 a={a},b={b}")

# 1、赋值运算符从右往左
# 2、赋值运算符的左边是变量，右边可以是变量、表达式、字面量