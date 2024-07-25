""""
"需求":
1 尝试只读方式打开text。txt文件,如果文件存在则读取文件测试内容，文件不存在则提示用户即可
2 读取内容要求：尝试循环读取内容，读取过程中如果检测用户意外终止程序,则except捕获异常并提示用户
"""
import time
try:
   file = open("test.txt","r")
# 尝试循环读取内容
   try:
     while True:
         con=file.readline()
    # 如果读取完成退出循环
         if len(con)==0:
            break
         time.sleep(1)
         print(con)
   except:
     print("程序被意外终止！")
except:
    print("该文件不存在！")
