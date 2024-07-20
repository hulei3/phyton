s2 = {10,20,30,40,50}
# 2.删除
# 2remove():删除指定数据，不存在就会报错
# s2.remove(10)
# print(s2)

# 2 discard():删除指定数据，不存在就会不报错
# s2.discard(10)
# print(s2)
# s2.discard(10)
# print(s2)

# 2.3 poo():随机删除某个数据，并且返回这个删除的数据
del_num = s2.pop()
print(del_num)
print(s2)
