class Washer():
    def wash(self):
        print("正在洗衣服！")

    # 在类里面获取实例属性
    def print_info(self):
        # self.属性名
       print("洗衣机的宽度是{self.width}")
       print("洗衣机的高度是{self.height}")


haier=Washer()

# 添加类型名、属性名
haier.width = 400
haier.height = 500

# 在类外面获取对象属性 对象名.属性名=值
# print(f"洗衣机的宽度是{haier.width}")
# print(f"洗衣机的高度是{haier.height}")

# 对象需要调用实例方法，才可以把对象的事自动传递到实例方法
haier.print_info()






