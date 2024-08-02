# “需求”： 将小于房子剩余面积的家具摆放到房子中
"""
分析：
房子类
实例属性
1. 房子的地理位置
2. 房子的占地面积
3. 房子的剩余面积
4. 房子中家具列表
实例方法： 容纳家具
显示房屋的信息: _ str _
家具类
1. 家具名称
2. 家具占地面积
"""
class Furniture( object):
    def __init__(self):
        # 家具名称
        self.name=name
        # 家具占地面积
        self.area=area

class Home(object):
    def __init__(self,address,area):
        # 1.房子的地理位置
        self.adress=adress
        # 2.房子的占地面积
        self.area=area
        # 3.房子的剩余面积
        self.free_area=area
        # 4. 房子中家具列表
        self.furniture=[]

    # 添加家具的实力方法
    def add_furniture(self):
        pass

    #添加家具的实例方法
    def _add_furniture(self, item):  #. item表示的是bed这一个对象
        #如果说家具的占地面积<=房子的剩余面积：可以搬进去(家具列表中添加家具并且更新房子的剩余面积
        #房屋的面积-添加的家具的占地面积)，否则去提示用户家具太大，剩余面积不足，无法容纳
        if item.area<= self.free_area:
           self.furniture.append(item.name)
           self.free_area -= item.area
        else:
           print(f"{item.name}")

    def __str__(self):
       return f"房子的地理位置在{self.address},"f"房屋面积是{self.area},"f"剩余面积是{self.free_area},"f"家具有(self.furniture)

#家具的实例
bed = Furniture("双人床", 20)
sofa = Furniture("沙发", 10)
homel = Home("北京", 1000)
homel. add_furniture(bed)
print(home1)








I