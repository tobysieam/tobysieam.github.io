# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :11_数据类型转换问题.py
# @Time     :2024/6/16 上午11:21

n1 = 100
result = "n1的值是："
print("result")

# 1、Python变量的类型不是固定的，会根据变量当前值在运行时决定的，可以通过内置函数type（变量）来查看其类型，这种方式就是隐式转换，有的书也称为自动转换

#Python根据该变量使用的上下文在运行时决定的
var1 = 10
print(type(var1))
var1 = 1.1
print(type(var1))

# 在运算的时候，数据类型会向高精度转换，float的精度高于int
var2 = 10
var3 = 1.2
var4 = var2 +var3
print("var4=",var4,"var4的类型:",type(var4))
var2 = var2 + 0.1
print("var2=",var2,"var2的类型：",type(var2))

# 2、显式类型转换
# 如果需要对变量数据类型进行转换，只需要将数据类型作为函数名即可，这种方式就是显式转换/强制转换
# 以下几个内置函数可以完成数据类型之间的转换。函数会返回一个新的对象/值，就是强制转换后的结果

i=10
j=float(i)
print("j的类型:",type(j),"j=",j)
k=str(i)
print("k的类型:",type(k),"k=",k)

# 显式类型转换注意：一切皆为对象
# 1、不管什么值的int，float都可以转换成str，str(x)将对象x转换成字符串
n1 = 100
n2 = 123.65
print(str(n1))
print(str(n2))

# 2、int转换成float是，会增加小数部分，比如123->123.0，float转换成int时，会去掉小数部分，比如123.65->123
print(float(n1)) #100.0
print(str(n2)) #123



