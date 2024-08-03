import threading

thread = threading.Lock()
#需求：多线程同时根据下标在列表中取值，要保证同一时刻只能有一个线程去取值def get value(index):
#上锁
def get_value(index):
    thread.acquire()
    list1 = [1, 3, 5, 7]
    # 判断下标是否越界
    if index >= len(list1):
        print(f"下标越界:{index}")
        thread.release()
        return
    value = list1[index]
    print(value)
    # 释放锁
    thread.release()
if __name__=="__main__":
    # 创建多个线程，同时执行根据下标取值的任务
    for i in range(10):
        sub_thread = threading.Thread(target=get_value,args = (i,))
        sub_thread.start()

