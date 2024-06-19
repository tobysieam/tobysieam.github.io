# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :14_type_change_exercise.py
# @Time     :2024/6/19 下午9:47


i = 10
j = float(i)   #10.0
print(type(i)) #int
print(type(j)) #float

i=j+1
print(type(i)) #float
print(type(j)) #float

print(i)      #11.0
print(int(i)) #11
print(type(i)) #float