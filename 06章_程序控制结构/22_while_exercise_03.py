# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :22_while_exercise_03.py
# @Time     :2024/8/3 上午10:19

#一直输入姓名，直到输入为exit
# '''
# 思路：1、定义 变量name，接受用户输入
#      2、使用while判断，name!= exit循环输入即可
# '''

name = input("请输入名字：")
while name!="exit":
    name = input("请输入名字：")
    print("名字是",name)