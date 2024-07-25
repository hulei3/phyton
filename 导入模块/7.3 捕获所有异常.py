# 4 捕获所有异常，Exception是所有异常的父类
try:
    print(1/0)
except Exception:
     print("有错误！")


