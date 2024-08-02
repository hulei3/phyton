#·1. iter() : 用于创建迭代器对象
#2.next()：用于输出可迭代对象中的元素
#需求：在可迭代对象中遍历取值
list1 = [1, 2, 3, 4, 5]
#创建迭代器对象
# it = iter(list1)
it = list1. __iter__()
#遍历取值
# print(next(it))
# print(next(it))
# print(next(it))

try:
    while True:
        print(it.__next__())
except:
    print("取值过程中引发了stoplteration异常！")

