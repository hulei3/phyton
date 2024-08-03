import threading
num = 0

# 循环10次执行的任务
def test1():
    for i in range(10):
        global num
        num+=1
    print(f"test1:{num}")

# 循环10次执行的任务
def test2():
    for i in range(10):
        global num
        num+=1
    print(f"test2:{num}")

if  __name__ == "__main__":
    first_thread = threading.Thread(target=test1)
    second_thread = threading.Thread(target=test2)
    first_thread.start()
    second_thread.start()

