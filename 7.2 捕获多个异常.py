# try:
#     print(1/0)
# except (NameError,ZeroDivisionError):
 #    print("有错误！")

# 4 捕获异常描述形式
try:
   print(1/0)
except (NameError,ZeroDivisionError) as result:
    print(result)

