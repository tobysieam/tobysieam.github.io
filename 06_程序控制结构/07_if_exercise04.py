# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :07_if_exercise04.py
# @Time     :2024/7/13 下午6:52

# 定义两个int类型变量,判断二者的和,是否能被3又能被5整除,打印提示信息

num1 = 10
num2 = 2
if(num1 + num2) % 3 == 0 and (num1 + num2) % 5 == 0:
    print("True")
else:
    print("False")