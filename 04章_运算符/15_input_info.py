# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :15_input_info.py
# @Time     :2024/7/7 下午4:52

name = input("请输入姓名:")
age = input("请输入年龄:")
score = input("请输入成绩:")

print("\n输入的信息如下：")
print("name:",name)
print("age:",age)
print("score:",score)

# 注意，控制台接收到的数据是str
print(type(name))
print(type(age))
print(type(score))

# print(10+score) 报错了
# 如果我们需要对接收到的数据进行算术运算
print(10 + float(score))

# 当然也可以在接收数据时直接转成需要的类型
age = int(input("请输入年龄"))
print(type(age))
