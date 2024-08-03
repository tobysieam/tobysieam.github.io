# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :21_while_exercise_02.py
# @Time     :2024/8/3 上午10:16

#打印40-200之间的偶数
# '''
# 思路：1、定义 i= 40，max_num = 200,表示我们要遍历的范围
#      2、如果i%2 == 0，说明 i 可以被3整除
#      3、满足条件输出即可，注意i+=1
# '''

i = 40
num_max = 200
while i < 200:
    if i%2 == 0:
        print(i)
    i+=1
