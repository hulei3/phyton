# 装饰器:就是给已有函数增加额外功能的函数，它本身就是一个闭包函数
# 如果外部函数的参数有且只有一个并且是函数类型在内部函数使用的话，那么这个闭包函数就是装饰器
def decorator(func):
    def inner():
        func
        #在内部函数内对已有的函数进行装饰
        print("恭喜你登录成功！")
    return inner

def comment():
    print("请输入密码！")
    # print("恭喜你登录成功！")

comment()

# 使用装饰器装饰已有的函数
new_func=decorator(comment)
new_func()