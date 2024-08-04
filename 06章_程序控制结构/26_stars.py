# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :26_stars.py
# @Time     :2024/8/4 上午9:55

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
# '''

"""
1、打印矩形
*****
*****
*****
*****
*****

2、打印直角三角形
*
**
***
****
*****

3、打印金字塔
    *       2*1-1  空格4 5-1
   ***      2*2-1  空格3 5-2
  *****     2*3-1  空格2
 *******    2*4-1
*********   2*5-1

4、打印空心金字塔
    *          分析、每层的两边输出*，最后一层输出*
   * *
  *   *
 *     *
*********

5、总层数、total_level
"""

total_level = 5

#first
# #i控制层数
# for i in range(1,6):
#     # j控制每行输出的星号数
#     for j in range(1,6):
#         #这里的end=""，表示输出不换行
#         print("*",end="")
#     #每行输出后，换行
#     print("")


# #second
# #i控制层数
# for i in range(1,6):
#     # j控制每行输出的星号数
#     for j in range(1,i+1): #或者range(i)也可以
#         #这里的end=""，表示输出不换行
#         print("*",end="")
#     #每行输出后，换行
#     print("")

# #third
# #i控制层数
# for i in range(1,6):
#     #k控制输出的空格数
#     for k in range(5-i):
#         print(" ",end="")
#     # j控制每行输出的星号数
#     for j in range(2*i-1):
#         #这里的end=""，表示输出不换行
#         print("*",end="")
#     #每行输出后，换行
#     print("")

#fourth
for i in range(1,6):
    #k控制输出的空格数
    for k in range(5-i):
        print(" ",end="")
    # j控制每行输出的星号数
    for j in range(2*i-1):
        #这里的end=""，表示输出不换行
        if j == 0 or j ==2 * (i-1) or i == 5:
            print("*",end = "")
        else:
            print(" ",end="")
    #每行输出后，换行
    print("")

#fifth
for i in range(1,total_level+1):
    #k控制输出的空格数
    for k in range(total_level-i):
        print(" ",end="")
    # j控制每行输出的星号数
    for j in range(2*i-1):
        #这里的end=""，表示输出不换行
        if j == 0 or j ==2 * (i-1) or i == 5:
            print("*",end = "")
        else:
            print(" ",end="")
    #每行输出后，换行
    print("")