# 可变类型:列表
aa=[11,22]
bb=aa
print(aa)
print(bb)
print(id(aa))
print(id(bb))

# 修改aa得值
aa.append(33)
print(aa)
print(bb)
print(id(aa))
print(id(bb))