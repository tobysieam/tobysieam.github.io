# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :19_while_else.py
# @Time     :2024/8/3 上午10:02

#while else使用案例

i = 1
while i<3:
    print("hello")
    i += 1
    if i == 2:
        break
else:
    print("i<3不成立")