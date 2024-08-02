#自定义迭代器类，迭代器协议：1，有iter(返回的迭代器对象)2.next(返回下一个元素)方法
# class A(object):
 #   def __init__(self):
 #       self.num=0

 #   def info_print(self):
 #       self.num=1
  #      return self.num

# a=A()
# for i in a:
 #    print(i)

class B(object):
     def __init__(self):
         self.num=0
         return self

     # 返回下一个元素
     def __next__(self):
         self.num +=1
         return self.num

b =B()
# print(next(b))
it =iter(b)
print(next(it))