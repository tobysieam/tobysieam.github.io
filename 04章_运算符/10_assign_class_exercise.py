# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :10_assign_class_exercise.py
# @Time     :2024/7/6 下午9:55

# 不使用前面两种方式交换变量a和b
a = 1
b = 2
print(f"a={a} b={b}")
a = a+b
b = a-b
a = a-b
print(f"a={a} b={b}")
# 以一种算法实现
