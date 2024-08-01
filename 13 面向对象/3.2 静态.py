# 定义类:定义一个静态方法
class Dog(object):
    @staticmethod
    def info_print():
        print("这是一个静态方法！")

# 2 创建对象，用静态方法:类和对象
wangcai=Dog()
Dog.info_print()
wangcai.info_print()