'''
特点 ：a 集合中的数据不重复
    b 集合是无序,不支持下标操作
'''

# 1 创建空集合
# s1=set()
# print(s1)
# print(type(s1))

# s2={}#不能用来创建空集合，创建空集合只能用你set()
# print(s2)
# print(type(s2))

# 2 创建有数据的集合
# s3={10,20,30}
# print(s3)
# print(type(s3))

# 集合内的数据去重,并且无序
# s4={10,30,40,20,50.20,10,20}
# print(s4)
# print(type(s4))

s5=set("abcdef")
print(s5)
print(type(s5))
