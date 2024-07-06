# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :13_type_change_detail.py
# @Time     :2024/6/16 上午11:50


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
# print(float(n4)) 报错
# print(int(n4))   报错

# 4、对一个变量进行强制转换，会返回一个数据/值，强制转换后，并不会影响原变量的数据类型（即：不会影响原变量指向的数据/值的数据类型）
i = 10
j = float(i)
k = str(i)
print("i的值：",i,"i的类型",type(i))
print("j的值：",j,"j的类型",type(j))
print("k的值：",k,"k的类型",type(k))