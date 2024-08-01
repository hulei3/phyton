class MusicPlayer(object):
    # 记录第一个被创建的对象的引用
    instance=None
    def __new__(cls,*args,**kwargs):
        if cls.instance is None:
        # 调用父类objecct的同名方法，可以为对象做到分配内存空间
           cls.instance = super().__new__(cls)

# 创建多个不同对象
player1=MusicPlayer()
print(player1)
player2=MusicPlayer()
print(player2)
player3=MusicPlayer()
print(player3)