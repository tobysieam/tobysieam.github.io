# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :07_or_operator.py
# @Time     :2024/7/6 下午9:27

# or运算符的使用
#定义一个成绩变量
score = 70
# 判断成绩
print(score <= 60 or score >= 80)
if(score <= 60 or score >= 80):
    print("hi~")

a = 1
b = 99
print(a or b)
print((a>b) or b)
print((a<b) or b)

# or也是一个“短路运算符 ”，只有第一个为false才去验证第二个（换言之，如果第一个为true，就直接返回第一个的值）
