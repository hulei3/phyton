# “快速体验”:需求:尝试以r（读取）模式打开文件，如果文件不存在，则以w(如果文件不存在就创建方式）打开
"""
"语法“：
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
"""
try:
    file=open("test.txt","r")
except:
    file=open("test.txt", "w")