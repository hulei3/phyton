'''''
构成条件：
1 在函数内嵌套（定义函数再定义函数）的前提下
2 内部函数是用了外部函数的变量或参数
3 外部函数返回了内部函数
'''
def config_name(name):
    def inner(msg):
     print(name+":"+msg)
    return inner

tom=config_name("tom")
jerry=config_name("jerry")

tom("小姐妹，过来玩呀！")
jerry("不去！")
tom("有小哥哥!")
jerry("马上到！")


