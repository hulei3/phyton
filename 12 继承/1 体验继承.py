# object是所有类的父类和顶级类,基类，其他类就叫做原生类
# 准备第一个类，父类
class A(object):
    def __init__(self):
        self.num=1
    def info_print(self):
        print(self.num)

# 2 准备第二个类，子类
class B(A):  # B(A)就是B类去继承A类
    pass # 占位符，可以类中即便没有代码也不会报错

# 3 第3个类创建出来的对象去使用第一个类属性和方法
result = B()
result.info_print()