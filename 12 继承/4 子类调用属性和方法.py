# 定义:师傅类，属性和方法
class Master(object):
    def __init__(self):
        self.jishu="{古代煎饼果子配方}"

    def make_cake(self):
        print(f"运用了{self.jishu}煎饼果子")

        def a(self):
            print(1)

class School(Master):
    def __init__(self):
        self.jishu="{六星煎饼果子配方}"

        def make_cake(self):
            print(f"运用了{self.jishu}煎饼果子")

        def b(self):
            print(2)

    # 在子类
# 2.定义:定义徒弟类，继承师傅类
class Prentice(School,Master):
    def __init__(self):
        self.jishu="{古代煎饼果子配方}"

    def make_cake(self):
        print(f"运用了独创{self.jishu}煎饼果子")

        # 在子类中调用父类的同名方法
    def make_master_cake(self):
           # 父类类名.函数（）
     Master.__init__(self)
     #  print(self)
     Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
     #  print(self)
        School.make_cake(self)
class  Tusun(Prentice):
    pass
xiaotom=Tusun()
xiaotom.make_cake()
xiaotom.make_master_cake()
xiaotom.make_school_cake()
# 3.定义:使用徒弟类创建对象，调用师傅类的属性和方法
# tom=Prentice()
# print(tom.jishu)
# tom.make_cake()
# tom.make_master_cake()
# tom.make_school_cake()