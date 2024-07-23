def testA(a, b):
    print(a+b)


# 测试模块
# testA(1, 2)
# _name_是系统变量，如果在当前文件中使用，值是__main__,否则就是当前模块的名字
# print(__name__)
if __name__=="__main__":
     testA(1,2)