# 带if的列表推导式，创建一个有1-10的列表
# range():步长实现
#  list1=[i for i in range(1,11,2)]
# print(list1)

# 2 for循环加if语句实现:
# list2=[]
 #    for i in range(1,11):
 #   if i % 2 ! = 0:
 #        list2.apppend(i)
 # print(list2)

# 3 改变写if的列表推导式
list3=[i for i in range(1,11) if i %2 !=0]
print(list3)
