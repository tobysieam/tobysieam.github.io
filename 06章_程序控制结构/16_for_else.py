# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :16_for_else.py
# @Time     :2024/8/2 上午10:31

# for和else的配合使用

# for<variable> in <sequence>
#     <statements>
#   else:
#       <statements>

# 什么情况下会进入else，就是for循环正常的完成遍历，没有被打断（比如没有执行到break语句）
nums = range(1,4)
for i in nums:
    print("hello",i)
    if i ==2:
        break#中断了
else:
    print("没有循环数据了")

