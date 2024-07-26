# 1.装饰带有不定长参数和返回值的函数
# 定义函数
def decorator(func):
    def inner(a,b):
        print("正在努力执行加法运算.......")
        num = func(a,b)
        return num
    return inner

@decorator   # 等价于add num=decorator(add_num)
def add_num(num1,num2):
    result=num1+num2
    return result
    print(f"结果为:{result}")

result1=add_num(1,2)
print(f"结果是：{result1}")