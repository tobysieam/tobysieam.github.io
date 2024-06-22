# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :01_arithmetic_operator.py
# @Time     :2024/6/22 下午5:38

# 算术运算符的使用
# /,//,%,**

# 对于除号/，返回的结果是小数
print(10/3)

# 对于取整数//，返回商的整数部分（并且是向下取整）
print(10//3)
print(-9//2)
print(-10//3)

#当对一个数取模时，对应的运算公式：a%b=a-a//b*b
print(10 % 3)
print(-10 % 3)
print(10 % -3)
print(-10 % -3)

# 幂运算
print(2**5)
print(9**2)

print(97//7)
print(97%7)

c=234.5
print(5/9*(c-100))