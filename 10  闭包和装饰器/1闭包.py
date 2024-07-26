'''''
构成条件：
1 在函数内嵌套（定义函数再定义函数）的前提下
2 内部函数是用了外部函数的变量或参数
3 外部函数返回了内部函数
'''
# 构成闭包
def func_out():
    num1=10
    def func_inner(num2):
    # 内部函数使用了外部函数的变量或参数
     result=num1+num2
     print(result)

result=func_out()        # result=func_inner
result(1)
result(10)