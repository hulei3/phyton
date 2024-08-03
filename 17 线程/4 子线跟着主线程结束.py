import threading
import time
def test1():
    while True:
        print("任务执行中…")
        time.sleep(0.3)

if  __name__ =="__main__":
    sub_thread = threading.Thread(target=test1)
    # 让子线程设置成为守护主线程
    # sub _ thread. daemon = True
    # sub _ thread. setDaemon(True)
    sub_thread.start()

    time.sleep(1)
    sub_thread.join()
    print("主线程结束! ")


