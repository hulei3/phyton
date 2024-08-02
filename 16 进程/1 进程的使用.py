#1.导入进程包
import multiprocessing
import time
# 跳舞任务
def dance():
    for i in range(3):
        print("跳舞任务执行中…")
        time.sleep(0.5)
# 唱歌任务
def sing():
    for i in range(3):
        print("唱歌任务执行中…")
        time.sleep(0.5)
"""
1. group:指定进程组, 目前只能使用None
2. target:执行的目标任务名
3. name:进程名字
4.args以元组方式给执行任务传参
5. kwargs:以字典方式给执行任务传参
"""
if __name__  =="__main__":
    # 2. 调用进程包里面的Process类实例化对象,手动创建的进程是子进程
    dance_process = multiprocessing. Process(target=dance)
    sing_process = multiprocessing. Process(target=sing)
    # 3. 调用start()启动进程
    dance_process.start()
    sing_process.start()

#多个子进程之间执行是无序的，由操作系统调度决定的，调哪个就执行哪个
#主进程中执行唱歌任务，主进程在子进程执行之前
    sing()