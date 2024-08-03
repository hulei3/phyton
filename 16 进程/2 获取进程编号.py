#1.导入进程包
import multiprocessing
import time
import os
# 跳舞任务
def dance():
    # 获取当前的任务的进程编号
    dance_id = os.getpid()
    # 获取当前的任务是哪个进程对象: multiprocessing. current _ process()
    print(f"dance_id:{dance_id},{multiprocessing.current_process()}")
    dance_parent_id = os.getppid()
    print(f"dance process的父编号是: {dance_parent_id}")
    for i in range(3):
        print("跳舞任务执行中…")
        time.sleep(0.5)

# 唱歌任务
def sing():
    # 获取当前的任务的进程编号
    sing_id = os.getpid()
    # 获取当前的任务是哪个进程对象: multiprocessing. current_process()
    print(f"sing_id:{sing_id}, {multiprocessing.current_process()}")
    sing_parent_id = os.getppid()
    print(f"sing_process的父编号是: {sing_parent_id}")
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
if __name__ =="__main__":
    # 2. 调用进程包里面的Process类实例化对象,手动创建的进程是子进程
    dance_process = multiprocessing. Process(target=dance,name="dance_process")
    sing_process = multiprocessing. Process(target=sing,name="sing_process")
    # 3. 调用start()启动进程
    dance_process.start()
    sing_process.start()