# 全局变量:指的是在函数体内，外都能生效的变量
# 思考:如果有一个数据，在函数A,和函数B理使用。该怎么办？
# a1是全局变量，在函数体上声明的一个变量，就是全局变量
a1=100
def testA():
    print(a1)

def testB():
    a1=200
    print(a1)

testA()
testB()
print(a1)