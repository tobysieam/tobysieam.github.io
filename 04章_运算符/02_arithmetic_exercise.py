# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :02_arithmetic_exercise.py
# @Time     :2024/6/22 下午5:53

# 假如还有97天放假，合几个星期零几天
days=97
week=days//7
left_days=days%7
print(f"假如还有{days}天放假，合{week}星期零{left_days}天")

# 求出摄氏温度
hua_shi=234.5
she_shi=5/9*(hua_shi-100)
print(f"华氏温度{hua_shi}对应的摄氏温度{she_shi}")
print("华氏温度%.2f对应的摄氏温度%.2f"%(hua_shi,she_shi))
