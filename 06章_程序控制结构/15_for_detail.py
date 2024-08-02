# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :15_for_detail.py
# @Time     :2024/8/2 上午10:20

#range 函数
#class range(stop)
#class range(start,stop,step = 1)
#1、虽然被称作函数，但range实际上是一个不可变的序列类型
#2、range默认增加的步长step是1，也可以指定，start默认是0
#3、range()生成的数列是前闭后开 range(1,5)

# such as

r1 = range(1,6,1)
r2 = range(1,6)
r3 = range(1,11,2)

print("r1 = ",list(r1))
print("r2 = ",list(r2))
print("r3 = ",list(r3))