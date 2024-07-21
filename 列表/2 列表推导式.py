# 5多个for循环实现列表推导式。效果：[(1,0),(1,1),(1,2),(2,0），（2,1），（2，2）]
# 元组的数据1: 1 和2 range（1， 3）
# 元组的数据2: 0 1 2  range(3)
list1=[]
# for i in range(1,3):
#    for j in range(3):
#     # 列表里面添加元组
#       list1.append((i,j))
# print(list1)

# 多个for循环实现列表推导式
list2=[(i,j) for i in range(1,3) for j in range(3)]
print(list2)