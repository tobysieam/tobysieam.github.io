# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :28_stu_score.py
# @Time     :2024/8/5 上午9:47

#1、统计三个班的成绩情况，每个班有5名同学
#1) 求出各个班的平均分和所有班级的平均分，学生的成绩从键盘输入
#2) 统计三个班的及格人数
#思想：化繁为简、先死后活
# 1、统计一个班成绩请款，求出一个班平均分
# 2、统计三个班成绩情况，求出各个班平均分，所有班级平均分和及格人数

total = 0.0
pass_num = 0
class_num = 3
student_num = 5
# 循环处理三个班
for j in range(1,class_num+1):
    #统计一个班成绩情况，求出一个班平均分
    sum = 0.0
    for i in range(1,student_num+1):
        score = float(input(f"请输入第{j}班的第{i}个学生的成绩："))
        #判断是否及格，累加到pass_num
        if score >= 60.0:
            pass_num += 1
            #累加到sum
        sum += score
    print(f"第{j}个班级的情况：平均分{sum/5}")
    total += sum
# 输出所有班级的平均分和及格人数
print(f"所有班级平均分{total/(5*3)} 及格人数：{pass_num}")
