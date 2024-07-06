# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :03_compare_operator.py
# @Time     :2024/7/6 下午8:42

# 比较运算符的使用
a=9
b=8
print(a>b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
# 把a>b的值赋予flag
flag=a>b
print("flag =",flag)
print(a is b)
print(a is not b)
# 在交互模式下考虑字符串的驻留机制

str1 = "abc#"
str2 = "abc#"
print(a is b)