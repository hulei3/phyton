# 1
#class A(object):
 #   pass

# a=A()
# print(a)

#2
class B(object):
    def __new__(cls):
        # 重写父类的同名方法
        a=super().__new__(cls)
        print(a)
        return a
    def __init__(self):
        print("__init__被执行了！")

b=B()
print(b)



