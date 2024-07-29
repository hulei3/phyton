# __init__魔法方法
class Washer():
    def __init__(self):
        # 添加实例属性、对象名 对象名.属性名=值
        self.width = 400
        self.height = 800

        # 在实例方法中，访问实例属性
        def print_info(self):
            # self.属性名
            print(f"洗衣机的宽度是{self.width}")
            print(f"洗衣机的高度是{self.height}")

haier = Washer()
haier.print_info()
