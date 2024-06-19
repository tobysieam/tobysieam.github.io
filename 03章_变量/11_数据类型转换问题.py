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

# 3.在将str类型转换成基本数据类型时，要确保str值能够转成有效的数据，比如，我们可以把 "123"，转换成一个整数，但是不能把"hello"转成一个整数，如果格式不正确，程序会报ValueError，程序就会终止
n3 ="12.3"
print(float(n3)) #12.3
# print(int(n3)) 报错

n4 = "hello"
# print(float(n4))
# print(int(n4))

# 4、对一个变量进行强制转换，会返回一个数据/值，强制转换后，并不会影响原变量的数据类型（即：不会影响原变量指向的数据/值的数据类型）
i = 10
j = float(i)
k = str(i)
print("i的值：",i,"i的类型",type(i))
print("j的值：",j,"j的类型",type(j))
print("k的值：",k,"k的类型",type(k))

