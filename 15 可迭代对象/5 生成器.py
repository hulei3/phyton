#·1.生成器表达式，类似列表推导式
# list1 = [i *2 for i in range(3)]
# print(list1)
#生成器第一种写法：生成器表达式
list1 = (i * 2 for i in range(3))
# print(list1)
print(next(list1))
print(next(list1))
print(next(list1))