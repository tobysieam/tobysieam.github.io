# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :29__num_break.py
# @Time     :2024/8/5 上午10:24

#随机生成1-100的一个数，直到生成了97这个数，看看一共用了几次
"""
思路：
1、定义变量count，统计一共用了多少次
2、使用while true无限生成随机数，直到生成97就退出
3、输出count即可

"""

# 导入random模块
import random

count = 0
while True:
     n = random.randint(1,100)
     count += 1
     if n == 97:
         break

print(f"生成97一共用了{count}次")