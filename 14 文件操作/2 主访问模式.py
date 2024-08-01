# 1. r表示只读，如果说文件不存在， 报错，并且不支持写入操作
# file = open(" test. txt", "r")
# file = open(" test1. txt", "r")
# file. write(" aaa")
# file. close()
#2. w表示只写，如果说文件不存在， 新建文件，执行写入，会用写内容覆盖原有内容
# file = open("test2. txt", "w")
# file.write("bbb")
# file. close()

#3.a表示追加，如果说文件不存在，新建文件，在原有内容的基础上追加新内容
file = open("test3. txt", "w")
file.write("bbb")
file. close()