# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :12_ternary_operator_exercise.py
# @Time     :2024/7/7 上午11:18

# 用if-else求出三个数的最大值
a = 10
b = 20
c = 30
max1 = a if a>b else b

max2 = max1 if max1>c else c
print(f"max2={max2}")

# 还可以使用一条语句嵌套使用完成
max = (a if a>b else b) if (a if a>b else b)>c else c
print(f"max={max}")