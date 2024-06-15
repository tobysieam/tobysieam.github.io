# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :09_str_detail.py
# @Time     :2024/6/15 下午3:24

# 介绍
# 1、字符串是Python中很常用的数据类型，通俗来说，字符串就是字符组成的一串内容
# 2、使用引号包括起来，创建字符串
# 3、str就是string的缩写，在使用type（）查看数据类型时，字符串类型显示的是str

# 字符串使用注意事项
# 1、使用引号（' 或 "）包括起来，创建字符串
str1="Tom说:\"hello\""
str1='Tom说:"hello"'
print(str1)

str2="Tom说:'hello'"
print(str2)

print(f"str2的类型:{type(str2)}")

# 2、通过加号连接字符串
print("hi+Tom")

# 3、Python不支持单字符类型，单字符在Python中也是作为一个字符串使用
# 4、用三个单引号'''内容'''或三个双引号"""内容"""可以使字符串内容保持原样输出，在输出格式复杂的内容是比较有用的，比如输出一段代码
print('''a small animal with fur, four legs, a tail, and claws, usually kept as a pet or for catching mice
猫''')

#5、在字符串前面加'r'可以使整个字符串不会被转义（比如输出文件地址）
str4=r"jack\ntom\tking"
print(str4)
