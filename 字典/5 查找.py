dict3 = {"name":"Tom","age":"20","geneder":"男"}
# 3 查找：a 按key查找  b: 按函数查找
# 3.1:字典序列名{key}
# print(dict3["age"])      # 存在，返回key对应的值
# print(dict3("ages"))      # 不存在，报错

# 3.2 get():存在返回key对应的值，不存在的话会反应值None
# print(dict3.get("name"))
# print(dict3.get("names"))
# print(dict3.get("names","maiya")) # 如果有两个数据，那么这个默认值返回第二个数据，并且返回第二个数据

# 3.3 keys:查找字典中所有的key，返回可迭代对象：用for循环的对象 比如：字符串、列表、元组、集合、字典
# print(dict3.keys)

# 3.4 values():查找字典中所有的值，即可迭代对象
# print(dict3.values())

# 3.5 items():查找所有对象的键值对，返回可迭代对象：每一个键值对都是放在元组中
print(dict3.items())





