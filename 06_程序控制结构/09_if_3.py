# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :09_if_3.py
# @Time     :2024/7/13 下午7:44

# 小头儿子参加Python考试，他和大头爸爸达成承诺
# 如果：
# 成绩为100分时，奖励一辆BMW
# 成绩为(80,99]时，奖励一台iphone111
# 成绩为[60,80]时，奖励一个ipad
# 其他时，没有奖励

score = int(input("请输入成绩【整数】:"))
if 0 <= score <= 100:
    if score == 100:
        print("奖励一辆BMW")
    elif score > 80 and score <= 99:
        print("奖励一台iPhone13")
    elif score >=60 and score <= 80:
        print("奖励一个iPad")
    else:
        print("啥也没有")
else:
    print(score,"不在0~100")
