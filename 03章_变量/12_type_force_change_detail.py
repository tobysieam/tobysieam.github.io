# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :12_type_force_change_detail.py
# @Time     :2024/6/16 上午11:49

# 2、显式类型转换
# 如果需要对变量数据类型进行转换，只需要将数据类型作为函数名即可，这种方式就是显式转换/强制转换
# 以下几个内置函数可以完成数据类型之间的转换。函数会返回一个新的对象/值，就是强制转换后的结果

i=10
j=float(i)
print("j的类型:",type(j),"j=",j)
k=str(i)
print("k的类型:",type(k),"k=",k)