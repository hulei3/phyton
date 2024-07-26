# 使用闭包修改外部函数的变量
def func_out():
    num1=10
    def func_inner():
        num1=20
        result=num1+10
        print(result)
    print(num1)
    func_inner()
    print(num1)
    return   func_inner

new_func=func_out()
new_func