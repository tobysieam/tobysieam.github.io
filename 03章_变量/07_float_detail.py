# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :07_float_detail.py
# @Time     :2024/6/15 下午2:29
import sys

# Python的浮点类型可以表示一个小数

n1=4.5
n2=-3.6
print("n1=",n1)
print("n2=",n2)

# 浮点类型的表示形式
n3=5.12
n4=.512
print("n4=",n4)

# 科学计数法形式：如5.12e2，5.12E-2
n5=5.12e2 #5.12乘十的二次方
n6=5.12E-2 #5.12除以10的二次方
print("n5=",n5)
print("n6=",n6)

# sys.float_info可以知道浮点类型支持的最大和最小数
# 浮点类型计算后，存在精度的损失，可以使用Decimal类进行精度计算

b=8.1/3
print("b=",b)

#1、 解决浮点数精度问题（使用Decimal类进行精度计算）
#2、 如果使用Decimal类，需要导入Decimal类
# 导入Decimal类
from decimal import Decimal

b=Decimal("8.1")/Decimal("3")
print("b=",b)