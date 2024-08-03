import threading
def show_info(name,age):
    print(f"name:{name}, age:{age}")

if __name__== "__main__":
    # 创建子线程
    # 以元组的方式传参，要保证参数的位置是一致的
    # 以字典的方式传参，要保证key名和函数的参数名一致
    # sub _ thread= threadirlg. Thread(target=show _ info, args=("tom", 20))
    sub_thread = threading.Thread(target=show_info, kwargs = {"name": "tom", "age": 20})
    sub_thread.start()

