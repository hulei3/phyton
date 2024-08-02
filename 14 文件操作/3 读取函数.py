# 1. read(num)
file=open("test1.txt", "r")
#read不写参数表示读取所有内容
# print(file. read())
# 底层代码中有\n，有字节占位
# file.close()

# 2readlines()
file=open("test1.txt", "r")
con=file.readlines()
print(con)
file.close()

# 3readline()
file=open("test1.txt", "r")
con=file.readline()
print(con)
file.close()
