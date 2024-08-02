# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :13_nested_if_example2.py
# @Time     :2024/7/13 下午10:47

# 出票系统：根据淡旺季的月份和年龄，打印票价[课后练习]
# 4-10 旺季：
# 成人（18-60）：60
# 儿童（<18）:半价
# 老人（>60）:1/3
# 淡季：
# 成人：40
# 其他：20

month = int(input("请输入月份："))
age = int(input("请输入年龄："))
if 4 <= month <= 10:#旺季
    if age > 60:
        print("价格为20")
    elif age >=18:
        print("价格为60")
    else:
        print("价格为30")
    print("OK")
else:#淡季
    if 18 <= age <= 60:
        print("价格为40")
    else:
        print("价格为20")