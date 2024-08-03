import threading
import time
list1=[]

def add_date():
    for i in range(3):
        list1.append(i)
        print(f"添加的数据是{list1}")
        time.sleep(0.3)

def read_date():
    print(f"读取的数据是{list1}")

if  __name__ =="__main__":
    add_thread = threading.Thread(target=add_date)
    read_thread = threading.Thread(target=read_date)
    add_thread.start()

    read_thread.start()
    print(list1)
# 线程之间共享全局变量
