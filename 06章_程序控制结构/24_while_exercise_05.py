# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :24_while_exercise_05.py
# @Time     :2024/8/3 上午10:40

#循环输出等式
# '''
# 思路：1、定义 一个变量num，接受用户的输入整数，定义 i = 0
#      2、遍历0-num，第一个加数是0-num，第二个加数是num-0
#      3、使用while循环完成即可
# '''

num = int(input("请输入一个整数："))
i = 0
while i<num:
    print(f"{i}+{num-i}={num}")
    i+=1