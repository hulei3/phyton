# "需求":警务人员和警务够一起合作，警犬分2分钟；追击敌人和追击毒品，警务人员携带不同的警犬，做不同的工作
# 1 定义父类，并提供公共方法
class Dog(object):
    def work(self):
        pass

# 2 定义子类，并重写父类方法
class ArmyDog(Dog):
    def work(self):
        print("追击敌人.....")

class DrugDog(Dog):
    def work(self):
        print("追击毒品.....")

# 定义人类
class Person(object):
    def work_with_dog(self,Dog):
       Dog.work()

 # 3 传递子类对象给调用者，可以看到不同子类执行效果的不同
aa = ArmyDog()
dd = DrugDog()
tom = Person()
tom.work_with_dog(aa)

# 作用:调用灵活，去适应需求不断变化