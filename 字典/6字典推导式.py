# a 创建一个空字典，字典key是1-5数字，value是这个数字2次方
dict1={i:i**2 for i in range(1,6)}
print(dict1)

# 将两个列表何为一个字典
list1=["name","age","id"]
list2=["Maiya",10,110]
dict2={list1[i]:list2[i] for i in range(len(list1))}
print(dict2)