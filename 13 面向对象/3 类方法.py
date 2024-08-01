# 定义类:定义类私有属性，类方法获取这个私有类属性
class Dog(object):
    _tooth=10

    # 定义类方法
    @classmethod
    def get_tooth(cls):
        print(cls)
        return cls._tooth

# 2 创建对象，使用类方法
wangcai=Dog()
result=wangcai.get_tooth()
# print(result)
print(Dog)
print(wangcai)