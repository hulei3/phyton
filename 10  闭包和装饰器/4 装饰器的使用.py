import time
# print(time.time())  # 获取的时间是以秒为单位，是距离1970，0.0.0时间差
# 定义装饰器:统计函数执行的时间
def decorator(func):
    def inner():
      # 在内部函数中对已有函数进行装饰:统计函数执行的时间
     # 获取函数执行前的时间
     begin= time.time()
     fun
      # 获取执行后的时间
     end=timc().time()
     result=end-begin
     print(f"函数执行完成所耗的时间:{result}")
     return innter
@decorator   # 等价于work=decorator(work)
def work():
    for i in range(1000):
        print(i)
 work()




