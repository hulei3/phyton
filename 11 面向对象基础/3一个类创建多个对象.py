# 一个类创建多个对象
# 通过多个对象去调用方法里面的时候，self地址是否相同
class washer():
    def wash(self):
        print("正在洗衣.....")
        print(self)

haier1=washer()
haier1.wash()

haier2=washer()
haier2.wash()

