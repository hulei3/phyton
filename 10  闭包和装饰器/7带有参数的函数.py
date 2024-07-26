# 定义装饰器
def return_decorator(flag):
    def decorator(func):
        def inner(a,b):
            if flag == "+":
               print("正在努力执行加法运算.......")
            elif flag == "-":
               print("正在努力执行减法运算.......")
            func(a,b)
        return inner
    return_decorator

# @return_decorator("+")
# 加法运算的函数
def add_num(a,b):
      result = a + b
      print(result)
add_num(1,2)

# @return_decorator("-")
# 减法运算的函数
def add_num(a,b):
      result=a-b
      print(result)
add_num(1,2)