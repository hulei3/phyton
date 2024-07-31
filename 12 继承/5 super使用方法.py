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
        self.jishu="{古代煎饼果子配方}"

    def make_cake(self):
        print(f"运用了独创{self.jishu}煎饼果子")

  # 在子类重写父母的同名属性和方法
  # 实现一次性调用父类的方法
    def make_old_cake(self):
  # 方法一:父类名，函数（）
        # School.__init__(self)
        # School.make_cake(self)
        # Master.__init__(self)
        # Master.make_cake(self)
      # 方法二:
  # 2.2 super(当前类名，self),函数（）
       # super(Prentice.self).__init__()
       # super(Prentice.self).make_cake()

    #2.2 super()无参数
        super().__init__()
        super().make_cake()
tom=Prentice()
tom.make_old_cake()