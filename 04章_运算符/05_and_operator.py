# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :05_and_operator.py
# @Time     :2024/7/6 下午9:00

#and运算符的使用
#定义一个成绩变量
score = 70
#判断成绩是否在60-80之间
print(score>=60 and score<=80)
if(score>=60 and score<=80):
    print("成绩还不错~")

# and 是“短路运算符 ”，只有当第一个是true时才去验证第二个
