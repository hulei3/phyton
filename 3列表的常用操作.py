name_list=["Maiya","XiaoLu","Panpan","maiya"]
# 需求：注册邮箱，用户输入一个账号名,判断这个账号是否存在，给出相应的提示
name=input("请输入你的邮箱账号名：")
if name in name_list:
    print("你输入的名字是{name}，此用户已经存在！")
else:
    print("你输入的名字是{name}，可以注册！")