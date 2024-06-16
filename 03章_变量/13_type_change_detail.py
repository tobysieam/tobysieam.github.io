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
