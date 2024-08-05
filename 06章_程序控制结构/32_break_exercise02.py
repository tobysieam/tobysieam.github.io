# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :32_break_exercise02.py
# @Time     :2024/8/5 上午10:56

# 实现登陆验证，有三次机会，假设用户名为”张无忌“，密码为”888“，提示登录成功，否则提示还有几次登录机会
"""
思路：
1、定义变量count,表示登录机会，使用for3次循环
2、接受用户输入，（name+pwd），如果满足条件就break
3、根据登录情况，提示还有几次登录机会

"""

count = 3

for i in range(1,count+1):
    name = input("请输入名字：")
    pwd = input("请输入密码：")

    if name == "张无忌"and pwd == "888":
        print("登录成功")
        break
    else:
        count -= 1
        print(f"你还有{count}次登录机会")