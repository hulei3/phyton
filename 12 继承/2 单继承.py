# “单继承”:值得是一个父类继承一个子类
# 定义:师傅类，属性和方法
class Master(object):
    def __init__(self):
        self.jishu="{古代煎饼果子配方}"
    def make_cake(self):
        print(f"运用了{self.jishu}煎饼果子")
# 2.定义:定义徒弟类，继承师傅类
class Prentice(Master):
    pass
# 3.定义:使用徒弟类创建对象，调用师傅类的属性和方法
tom=Prentice()
print(tom.jishu)
tom.make_cake()

# 单继承总结:一个父类继承一个子类，一对一的继承是单继承