# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :23_while_exercise_04.py
# @Time     :2024/8/3 上午10:34

# 打印1-100是九的倍数的整数，统计个数，及其总和
#打印40-200之间的偶数
# '''
# 思路：1、定义 i = 1，max_num = 100,表示我们要遍历的范围
#      2、如果i%9 == 0，说明 i 可以被9整除
#      3、定义count来统计个数，定义sum来计算总和，注意i+=1
# '''

i = 1
count = 0
sum = 0
max_num = 100
while i<max_num:
    if i % 9 ==0:
        print(i)
        count +=1
        sum += i
    i+=1

print(count)
print(sum)
print(f"count={count} sum={sum}")