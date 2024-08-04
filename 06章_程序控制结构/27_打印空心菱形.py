# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :27_打印空心菱形.py
# @Time     :2024/8/4 上午10:31

#打印空心金字塔

# '''
# 思路：
# -先死后活
# 1、先不考虑层数变化，假定就是五层，后面做活
# -化繁为简
# 1、打印矩形
# 2、打印直角三角形
# 3、打印金字塔
# 4、打印空心金字塔
# 5、打印对称的部分，构成菱形
# '''


"""
1、打印矩形
*********
*********
*********
*********
*********
*********
*********
*********
*********

2、打印一个箭形
*
***
*****
*******
*********
*******
*****
***
*

3、打印金字塔
    *       2*1-1  空格4 5-1
   ***      2*2-1  空格3 5-2
  *****     2*3-1  空格2
 *******    2*4-1
*********   2*5-1
 *******
  *****
   ***
    *
4、打印空心菱形
    *
   * *
  *   *
 *     *
*       *   分析、每层的两边输出*，最后一层输出*
 *     *
  *   *
   * *
    *

5、总层数、total_level
"""

total_level = 10

#first
# #i控制层数
# for i in range(1,10):
#     # j控制每行输出的星号数
#     for j in range(1,10):
#         #这里的end=""，表示输出不换行
#         print("*",end="")
#     #每行输出后，换行
#     print("")


# #second
# #i控制层数
# for i in range(1,10):
#     # j控制每行输出的星号数
#     if i > 6:
#         i = 10 - i
#     for j in range(1,i+1): #或者range(i)也可以
#         #这里的end=""，表示输出不换行
#         print("*",end="")
#
#     #每行输出后，换行
#     print("")

# #third
# #i控制层数
# for i in range(1,10):
#     # j控制每行输出的星号数
#     if i >=6:
#         i = 10 - i
#     #k控制输出的空格数
#     for k in range(9-i):
#         print(" ",end="")
#     for j in range(2*i-1): #或者range(i)也可以
#         #这里的end=""，表示输出不换行
#         print("*",end="")
#
#     #每行输出后，换行
#     print("")


#fourth
#i控制层数
for i in range(1,10):
    # j控制每行输出的星号数
    if i >=6:
        i = 10 - i
    #k控制输出的空格数
    for k in range(9-i):
        print(" ",end="")
    for j in range(2*i-1): #或者range(i)也可以
        if j== 0 or j == 2*(i-1):
            # 这里的end=""，表示输出不换行
            print("*",end="")
        else:
            print(" ",end="")

    #每行输出后，换行
    print("")

#fifith
#i控制层数
for i in range(1,total_level+1):
    # j控制每行输出的星号数
    if i >=(total_level+1)/2:
        i = total_level + 1 - i
    #k控制输出的空格数
    for k in range(total_level-i):
        print(" ",end="")
    for j in range(2*i-1): #或者range(i)也可以
        if j== 0 or j == 2*(i-1):
            # 这里的end=""，表示输出不换行
            print("*",end="")
        else:
            print(" ",end="")

    #每行输出后，换行
    print("")


#其实和之前的金字塔题目类似，只是增加了 if i >=6 i = 10 - i