# 1 使用dir函数查看魔法方法
# class A(object):
 #   pass

# print(dir(A))

# 2 “__doc__":查看类的描述信息
# class B(object):
 #    """这是类的描述信息"""
 #   pass

# print(B.__doc__)

# 3. “_ module _”: 表示当前操作的对象在哪个模块
# 4. “_ class _”: 表示当前操作的对象的类是什么
import modulel
a = modulel.A()
a. func()

print(a. __module__)
print(a. __class__)
