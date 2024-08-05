# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :30_break_detail.py
# @Time     :2024/8/5 上午10:37

# break会终结最近的外层循环，如果循环有可选的else子句，也会跳过该子句

count = 0
while True:
    print("hi while")
    count += 1
    if count == 3:
        break
    while True:
        print("OK while")
        break
else:
    print("Hello while")

# 如果一个for循环被break终结，该循环的控制变量会保持其当前值
num = [1,2,3,4,5,6]
for i in nums:
    if i>3:
        break

print("i=",i)