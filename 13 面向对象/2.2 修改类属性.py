class Dog(object):
      tooth = 10

wangcai = Dog()
xiaohei = Dog()

# 1 类，语法，类，类属性=值
# Dog.tooth=20
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)

# 2 对象去修改类属性，语法，类，类属性=值
wangcai.tooth=200
print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

# 总结:如果想要添加类属性，那么只能通过类修改，如果是通过对象去修改的话，那么就是添加一个实例属性