# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :01_if_detail.py
# @Time     :2024/7/13 下午5:19

# if语句
# 1、当条件表达式为True时，就会执行代码块；如果为False，就不执行
# 2、Python缩进非常重要，是用于界定代码块的，相对于其他编程语言的大括号{}
if 4>1:
    print("ok1")
    print("ok2")

    print("ok3")

# 3、最短的缩进对较长的有包含关系，缩进前后没有要求
# 4、但是每个代码块应具有相同的缩进长度（TAB或者相同个数的空格）
if 100>20:
    print("ok4")
    print("ok5")
    if 8<2:
        print("ok6")
