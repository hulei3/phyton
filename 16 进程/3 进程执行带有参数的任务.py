import multiprocessing

def show_info(name,age):
    print(name, age)
#判断是否在主模块中执行
if __name__ == "__main__":
    # sub_process = multiprocessing.Process(target=show_info, args=("tom", 20))
    # sub_process= multiprocessing.Process(target=show_ nfo, kwargs={"name": "mai", "age": 20})
    sub_process = multiprocessing.Process(target=show_info, args=("tom",), 
    kwargs = {"age": 20})
    sub_process.start()
