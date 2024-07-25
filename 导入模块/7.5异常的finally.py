# 异常的finally:无论是否有异常需要执行的代码
try:
    file=open("test.txt","r")
except:
    file=open("test.txt", "w")
finally:
    file.close()