# 不可变类型:int、id():可以查看变量的内存地址
a=1
b=a
print(a)
print(b)
print(id(a))
print(id(b))

# 修改a的值数据测试id
a=2
print(a)
print(b)
print(id(a))
print(id(b))