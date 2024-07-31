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
           # super(School.self).__init__()
           # super(School.self).make_cake()
            super().__init__()
            super().make_cake()
    # 在子类
# 2.定义:定义徒弟类，继承师傅类
class Prentice(School):
    def __init__(self):
        # 共有权限
        # self.money = 2000
        # 私有权限，__money 就是私有属性
        self._money = 2000
        self.jishu="{独创煎饼果子配方}"
        # 获取私有属性
        def get_money(self):
            return self._money
        # 修改私有属性
        def set_money(self):
            self._money=3000

        # info_print()是私有方法
    def __info_print(self):
        print("这是私有方法！")

    def make_cake(self):
        print(f"运用了独创{self.jishu}煎饼果子")

tom=Prentice()
# print(tom.money)
#tom.info_print()
print(tom.get_money())
tom.set_money()
print(tom.get_money())