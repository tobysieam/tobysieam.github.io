# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :14_for_01.py
# @Time     :2024/8/2 上午9:45

# 打印十次“你好”
# 首先定义一个列表
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums,type(nums))

# for<变量> in <范围/序列>
#    <循环操作语句>

# 每次循环的时候，依次从nums中取值赋给i

for i in nums:
    print("你好",i)

#for i in [1,2,3]
    # print("你好",i)

print(nums,id(nums),nums[0],id(nums[0]))
# 证明内存引用（从底层的角度去看循环-取值（引用））
print(id(1))#1的地址相同，但是超过了某个数后地址会不同？