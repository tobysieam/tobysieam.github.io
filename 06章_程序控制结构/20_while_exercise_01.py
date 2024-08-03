# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :20_while_exercise_01.py
# @Time     :2024/8/3 上午10:08

#打印1-100所有能被3整除的数
# '''
# 思路：1、定义 i= 1，max_num = 100,表示我们要遍历的范围
#      2、如果i%3 == 0，说明 i 可以被3整除
#      3、满足条件输出即可，注意i+=1
# '''

i = 1
max_num = 100
while i < max_num:
    if i % 3 ==0:
        print(i)
    i+=1
