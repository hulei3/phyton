class MusicPlayer(object):
    # 记录第一个被创建的对象的引用
    instance=None
    # 记录是否执行初始化工作，Fasle代表执行没有执行
    init_flag=False
    def __new__(cls,*args,**kwargs):
        if cls.instance is None:
        # 调用父类objecct的同名方法，可以为对象做到分配内存空间
           cls.instance = super().__new__(cls)

        # 返回的是第一个对象创建时的内存地址
        return cls.instance
        def __init__(self):
            if MusicPlayer.init_flag is True:
                return
            print("播放器初始化！")
            # 修改类属性的标记
            MusicPlayer.init_flag = True

# 创建多个不同对象
player1=MusicPlayer()
print(player1)
player2=MusicPlayer()
print(player2)
