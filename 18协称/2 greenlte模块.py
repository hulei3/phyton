"""
1. 导入greenlet模块
2.实例化协程对象
3. 调用switch()函数
"""
# alt+ enter快捷键安装
import greenlet
from greenlet import greenlet

def sing():
    print("开始唱歌…")
    print("唱完了……")

def dance():
    print("开始跳舞…")
    print("跳完了……")

# 2. 实例化协程对象, greenlet(任务名)
greenl = greenlet(sing)
green2 = greenlet(dance)
# 3. 调用switch()函数,谁先调用谁先执行
greenl. switch()
green2. switch()
