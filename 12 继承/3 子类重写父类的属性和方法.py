# 定义:师傅类，属性和方法
class Master(object):
    def __init__(self):
        self.jishu="{古代煎饼果子配方}"

    def make_cake(self):
        print(f"运用了{self.jishu}煎饼果子")

        def a(self):
            print(1)

class school(object):
    def __init__(self):
        self.jishu="{六星煎饼果子配方}"

    def make_cake(self):
        print(f"运用了{self.jishu}煎饼果子")

        def b(self):
            print(2)

# 2.定义:定义徒弟类，继承师傅类
class Prentice(school,Master):
    def __init__(self):
        self.jishu="{古代煎饼果子配方}"

    def make_cake(self):
        print(f"运用了独创{self.jishu}煎饼果子")

# 3.定义:使用徒弟类创建对象，调用师傅类的属性和方法
tom=Prentice()
print(tom.jishu)
tom.make_cake()

# 总结:如果子类和父类有同名的属性和方法的时候，子类创建对象去调用属性和方法，调用到是子类的属性和方法

# 拓展:_mro_:可以用来站看某个类和方法
print(Prentice.__mro__)