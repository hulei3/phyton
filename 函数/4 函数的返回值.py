# 定义一个函数，返回值，如：
def buy():
    print("烟")
    return"烟"
   # print("烟")  # 不能执行
goods=buy()
print(goods)

# return:返回结果给函数调用的地方
''''
return的作用:
1 负责函数的返回结果，返回结果给函数调用的地方
2 使用return就会退出当前的函数，导致retrun下放所有的代码（函数内部）不执行
'''
#  需求:制作一个技术器，计算任意两个数字之和的结果，并且返回结果给用户
def sum_num(a,b):
    return a+b

result=sum_num(2,2)
print(result)