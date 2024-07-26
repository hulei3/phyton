# 1.装饰带有不定长参数和返回值的函数
# 定义函数
def decorator(func):
    # 内部函数的类型和被装饰的函数类型是一样的
    def inner(*args,**kwargs):
        # 在内部函数已有函数进行装饰
        print("正在努力执行加法运算.......")
        num = func(*args,**kwargs)
        return num
    return inner
# 不定长参数:包括位置参数（元组），包括关键字参数（字典）
@decorator   # 等价于add num=decorator(add_num)
def add_num(*args,**kwargs):
    result=0
    for value in args:
        result += value
    for value in kwargs.values():
        result += value
    return result

result1 = add_num(1,2,age=20,num=1)
print(f"结果是：{result1}")