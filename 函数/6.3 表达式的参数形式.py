# lambda 参数列表:表达式
# 1 表达式
# fn1=lambda:100
# print(fn1())

# 2,一个参数
# fn2=lambda a:a
# print(fn2("hello,world"))

# 3 默认参数/缺省参数
# fn3=lambda a,b,c=100:a+b+c
# print(fn3(10,20))
# print(fn3(10,20,30))

# 4可变参数/不定长参数:*args,包裹位置参数返回的是元组
# fn4=lambda *args:args
# print(fn4(10,20))
# print(fin4())

# **kwargs:包裹关键字参数,返回值是字典
fn5 = lambda  **kwargs:kwargs
print(fn5())
print(fn5(name="maiya",age=20))
