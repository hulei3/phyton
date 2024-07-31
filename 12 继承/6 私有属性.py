# 定义:师傅类，属性和方法
class Master(object):
    def __init__(self):
        self.jishu="{古代煎饼果子配方}"

    def make_cake(self):
        print(f"运用了{self.jishu}煎饼果子")

class School(Master):
    def __init__(self):
        self.jishu="{六星煎饼果子配方}"

        def make_cake(self):
            print(f"运用了{self.jishu}煎饼果子")
            super(School.self).__init__()
            super(School.self).make_cake()

    # 在子类
# 2.定义:定义徒弟类，继承师傅类
class Prentice(School):
    def __init__(self):
        self.jishu="{古代煎饼果子配方}"

    def make_cake(self):
        print(f"运用了独创{self.jishu}煎饼果子")
