# 需求:洗衣机  功能:洗衣机类
class washer():
    def wash(self):  # self指的是调用self所在方法的对象
        print("正在洗衣服！")
        print(self)

haier=washer()
print(haier)

haier.wash()