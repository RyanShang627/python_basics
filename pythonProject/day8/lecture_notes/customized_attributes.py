class Hero:
    def __init__(self, name, hp, mp=0):
        # 在类中封装实例属性
        # 名字
        self.name = name
        # 生命值
        self.hp = hp
        # 魔法值
        self.mp = mp
    def attack(self):
        print("英雄发起普通攻击")

    def move(self, x, y):
        print(f"执行移动英雄操作, x坐标为{x}, y坐标为{y}")

    def back_city(self):
        print("执行英雄回城操作")

    def a(self):
        # 使用实例属性: self.属性名
        print(self.name)
    def b(self):
        print(f"我的英雄名字是{self.name}, 我的hp是{self.hp}, 我的mp是{self.mp}")

    def c(self):
        # 在类的实例方法中：使用实例方法: self.方法名()
        self.attack()

hero1 = Hero("赵云", 200, 1000)
hero1.a()
hero1.b()
hero1.c()
# hero1.move(300, 210)
# print("--"*50)
#
# hero2 = Hero("刘备", 600, 100)
#
# hero3 = Hero("猪八戒", 10000)