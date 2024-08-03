""""
1. 创建锁: thread=threading. Lock()
2. 上锁: thread. acquire()
3. 释放锁: thread. release()
"""
import threading
num = 0
thread=threading.Lock()

# 循环100万次执行的任务
def test1():
    # 上锁
    thread.acquire()
    for i in range(1000000):
        global num
        num+=1
    print(f"test1:{num}")
    # 释放锁
    thread.release()

# 循环10次执行的任务
def test2():
    # 上锁
    thread.acquire()
    for i in range(1000000):
        global num
        num+=1
    print(f"test2:{num}")
    # 释放锁
    thread.release()

if  __name__ == "__main__":
    first_thread = threading.Thread(target=test1)
    second_thread = threading.Thread(target=test2)
    first_thread.start()
    second_thread.start()

