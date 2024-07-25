# 异常的else:如果没有异常需要执行的代码
try:
    print(1)
except Exception as result:
     print(result)
else:
    print("我没有异常时候执行的代码！")
