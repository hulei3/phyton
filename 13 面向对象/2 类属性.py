# 1 定义类，定义类属性
class Dog(object):
    # 1 定义类属性
     tooth=10
    # 定义实例属性
     def __init__(self):
        self.tooth1 = 20

# 2 创建对象
wangcai=Dog()
xiaohei=Dog()

# 3 访问类属性:类和对象
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)

# 3 访问实例属性:类和对象
# print(Dog.tooth1)  # 不能访问，报错
print(wangcai.tooth1)
print(xiaohei.tooth1)

# 总结:类可以去访问类属性，但是不能访问实例属性，而对象都可以是访问的