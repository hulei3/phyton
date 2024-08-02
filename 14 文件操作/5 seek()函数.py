# 0开头1当前位置2结尾
file=open("test1.txt","r+")
file=open("test1.txt","a+")
 # file seek()
# 在r+模式下把文件指针推送到结尾，无法读取数据
# file seek(0 2)
# 在a+模式下把文件指针推送到开头
file.seek(0,0)
con=file.read()
print(con)
file.close()