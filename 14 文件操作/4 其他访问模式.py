# r+，w+，a+ 的作用都是可以又读又写， 区分它们之间的区别
# r+:没有访问的文件会报错，文件指针在开头，所以读取诗句
# file=open("test3.txt","r+")
# file=open("test3.txt","r+")
# con=file.read()
# print(con)
# file.close()

# w+:没有访问的该文件新建文件，文件指针在开头，用新的内容覆盖原有的内容
# file=open("test3.txt","w+")
# file=open("test4.txt","w+")

#file.close()

# a+:没有访问的该文件新建文件，
file=open("test4.txt","a+")
file=open("test5.txt","a+")
con=file.read()
print(con)
#file.close()