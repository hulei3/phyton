#1.导入线程模块
import threading
import time

def sing():
    # 获取执行当前任务的线程对象

    current_thrend = threading.current_thread()
    print(f"sing thrend:{current_thrend}")
    for i in range(3):
        print("唱歌中……")
        time.sleep(0.2)

def dance():
    current_thrend = threading.current_thread()
    print(f"dance thrend:{current_thrend}")
    for i in range(3):
        print("跳舞中……")
        time.sleep(0.2)
if __name__=="__main__":
   # 2， 通过Thread类实例化对象，创建子线程
   sing_thread= threading.Thread(target=sing)
   dance_thread = threading.Thread(target=dance)
   # 3. 调用start函数启动子线程
   sing_thread.start()
   dance_thread.start()

# 多线程的执行是无序的，由cpu调度决定