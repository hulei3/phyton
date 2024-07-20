name_list=["Maiya","XiaoLu","Panpan",]
# 增加：增加指定数据到列表当中，列表的数据是可变的，列表是可变数据类型
# append():在列表的结尾追加数据 写法:序列名.append(数据)
name_list.append("huawei")
name_list.append("12.90")
print(name_list)

# extend:增加列表的结尾追加数据，如果是序列的话，会把序列的数据逐一添加  写法:序列.extend（数据）
name_list.extend("xiaomi")
print(name_list)

# insert():指定的位置增加数据，写法:序列名，insert(位置下标，数据）
name_list.insert(2,"h")
print(name_list)
