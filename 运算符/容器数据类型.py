str1="abcd"
list1=[1,2,3,4]
t1={10,20,30,40}
set1 = {100,200,300,400}
dict1={"age":20}
# 1 tuple():将序列转换成元组
# print(tuple(str1))
# print(tuple(list1))
# print(tuple(t1))
# print(tuple(set1))
# print(tuple(dict1))

# list():将序列转换成列表
print(list(t1))
print(list(set1))
print(list(dict1))

# 3 将序列转换成集合
print(set(t1))
print(set(set1))
print(set(dict1))