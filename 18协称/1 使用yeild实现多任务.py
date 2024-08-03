import time
"""
yiold的注意点:
1. 作用是类似于return， 后面可以接返回值
2.任何一个带有yield语句的函数都是生成器函数
"""
def test1():
    while True:
        print("----1----")
        time.sleep(0.1)
        yield

def test2():
    while True:
        print("----2----")
        time.sleep(0.1)
        yield

#函数中有yield语句，直接调用内部代码不执行
#创建生成器对象
def main():
    t1 = test1()
    t2 = test2()
    while True:
        next(t1)
        next(t2)

main()
#总结：使用yield实现的多任务效果，是在一个单线程下使用并发的执行方式实现的多任务，就是协理

















