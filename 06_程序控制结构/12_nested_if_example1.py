# @Version  : 1.0
# @Author   : Cheng Huang
# @File     :12_nested_if_example1.py
# @Time     :2024/7/13 下午10:38

# 参加歌手比赛，如果初赛成绩大于8.0进入决赛，否则提示淘汰
# 并且根据性别提示进入男子组或女子组。【可以让学员先联系下】
# 输入成绩和性别，进行判断和输出信息

score = float(input("请输入成绩："))
if score > 8.0:
    print("OK")
    gender = input("请输入性别（男|女）：")
    if gender == "男":
        print("小伙伴进入男子组决赛")
    else:
        print("小伙伴进入女子组决赛")
else:
    print("成绩不达标，淘汰")
