# 4 通用装饰器
def decorator(func):
    def inner(*args,**kwargs):
        print("正在努力执行加法运算.......")
        num = func(*args,**kwargs)
        return num
    return inner

@decorator
def show():
   return "你好！"
result=show()
print(result)