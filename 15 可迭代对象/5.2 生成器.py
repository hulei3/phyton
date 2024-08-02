#生成器第二种写法：生成器函数
# yield和return的作用一模一样，但是return在函数中后面是不能放执行代码， 所以使用yield
def test():
    print("开始生成! ")
    yield 1.
    yield 2
    yield 3

num = test()
print(next(num))
print(next(num))
print(next(num))