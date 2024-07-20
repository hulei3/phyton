# 枚举函数：enumerate(可遍历对象，start=0),数据2可以不写，通常和循环搭配
# 返回的结果是元组，第一个数据是原迭代对象的数据对应的下标，第二个数据是原迭代对象的数据
list1=["a","b","c","d","e"]
for i in enumerate(list1):
    print(i)