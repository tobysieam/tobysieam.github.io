# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :11_if_elif_else_exercise.py
# @Time     :2024/7/13 下午10:10

# 大家都知道，男大当婚，女大当嫁。那么女方家长要嫁女儿，当然要提出一定的条件：
# 高：180cm以上；富：财富一千万以上；帅：是。条件从控制台输入。
# 如果这三个条件都满足，则：“我一定要嫁给他！”
# 如果三个条件有为真的情况，则：“嫁吧，比上不足，比下有余。”
# 如果三个条件都不满足，则：“不嫁！”

height = float(input("身高（cm）："))
money = float(input("钱（万）："))
handsome = input("颜值（帅，不帅）：")

if height > 180 and money >1000 and handsome == "帅":
    print("我一定要嫁给他!")
elif height > 180 or money > 1000 or handsome =="帅":
    print("嫁吧，比上不足，比下有余。")
else:
    print("不嫁!")
