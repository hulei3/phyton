import threading
import time

def test1():
    time.sleep(1)
    # 获取执行当前任务的线程
    print(threading.current_thread())

if __name__ =="__main__":
    # 循环创建多个线程，测试线程之间执行是否无序
    for i in range(10):
        sub_thread = threading.Thread(target=test1)
        sub_thread.start()


