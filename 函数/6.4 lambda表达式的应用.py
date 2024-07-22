# 需求:lambda表达式比较两个数的大小，谁大返回谁
# lambda 参数列表:表达式
# fn1=lambda a,b: a if a>b else b
# print(fn1(10,15))

# 列表数据按字典key数据进行排序
students = {{"name":"maiya","age":20},{"name":"xiaowang","age":18},{"name":"xiaohai","age":19}}
# sort(key=None,reverse=Fasle)
# key=None:可以指定迭代对象中的一个元素进行排序
students.sort(key=lambda x:x["name"],reverse=Fasle)
print(students)