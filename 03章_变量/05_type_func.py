# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :05_type_func.py
# @Time     :2024/6/12 21:29

# 函数type()的使用

name = "Tom"   #字符串
gender = "男"  #字符串
age = 190.3   #浮点型
score = "100" #整型
is_todo = True #布尔类型

print(type(name))
print(type(gender))
print(type(age))
print(type(score))
print(type(is_todo))

#type可以直接查看具体的值（字面量）的类型
print(f"hello的类型是{type("hello")}")
print(f"1.1的类型是{type(1.1)}")
print(f"100的类型是{type(100)}")
print(f"True的类型是{type(True)}")