"""
1.导入gevent模块
2.实例化协程对象，需要调用spawn函数
3. 调用join()函数或者joinall(协程对象列表)
"""
# 1. 导入gevent模块
import gevent

def eat():
    print("要不要吃点东西? ")
    print("吃臭豆腐吧!")
def play():
    print("要不要玩点什么? ")
    print("去橘子洲吧! ")
# 2. 实例化协程对象,,需要调用spawn函数, spawn(任务名)
gevent1 = gevent.spawn(eat)
gevent2 = gevent.spawn(play)
# 3. 调用join()函数
gevent1.join()  # 等待gevent 1的任务执行结束
gevent2.join()  #等待gevent2的任务执行结束