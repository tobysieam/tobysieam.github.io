# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :03_format_output.py
# @Time     :2024/6/12 17:33

# 格式化输出案例
# 定义变量

age = 80
score = 90.5
gender = '男'
name = "Huang"
# str_string字符串

# %操作符输出
print("个人信息: %s %d %s %.2f" % (name,age,gender,score))

# format()函数
print("个人信息：{} {} {} {}".format(name,age,gender,score))

# f-strings[推荐]
print(f"个人信息: {name} {age} {gender} {score}")