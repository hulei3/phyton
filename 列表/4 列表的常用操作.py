name_list = ["Maiya","XiaoLu","Panpan"]
# 删除:删除列表指定的数据
# 1 del 删除目标 : 删除整个序列
#del name_list
# 可以删除制定下标的数据
# del name_list[0]
# print(name_list)

# 2 pop():删除指定下标的数据，不指定，默认会删除最后一个，并返回数据
# del_name=name_list.pop[]
# del_name= name_list.pop(1)
# print(name_list)

# 3 remove:删除列表中数据第一个匹配项
# name_list.remove("Maiya")
# print(name_list)

# 4clear():清空列表
name_list.clear()
print(name_list)