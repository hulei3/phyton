# "多继承":意识就是一个类同时继承多个父类
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
    pass
# 3.定义:使用徒弟类创建对象，调用师傅类的属性和方法
tom=Prentice()
print(tom.jishu)
tom.make_cake()

# 在多继承中，如果有一个类有多个父类的话，我去继承第一个父类的属性和方法