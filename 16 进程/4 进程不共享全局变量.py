import multiprocessing
import time

#定义全局变量
list1=[]
#添加数据的任务
def add_data():
    for i in range(3):
        listl.append(i)
        print(f"添加的数据是{i}")
        time.sleep(0.3)
# 读取数据的任务
def read_data():
    print(f"读取的数据是{list1}")

if __name__=="__main__":
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)
    add_process.start()
    read_process.start()