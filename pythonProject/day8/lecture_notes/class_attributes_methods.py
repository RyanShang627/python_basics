class Hero:
    # 类中定义的变量就是类属性
    b = 88 # b就是Hero类的属性
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

    # 定义类方法：使用装饰器@classmethod
    @classmethod
    def c(cls): # cls当前类的名字: Hero
        print("释放英雄技能")


hero1 = Hero("赵云", 200, 1000)
# 类属性对象和类都能调用
print(hero1.b) # 88
# 类名.类属性名
print(Hero.b) # 88
# 类不能调用实例属性
print(Hero.a) # AttributeError: type object 'Hero' has no attribute 'a'
# 总结：对象可以使用实例属性和类属性; 类只能使用类属性，不能调用实例属性
# 类方法和实例方法：对象可以调用实例方法和类方法；类只能调用类方法，不能调用实例方法
hero1.c()
Hero.c()
Hero.move(1, 2) # 如果类需要调用实例方法，必须给一个实例对象: Python当中一切皆对象，比如数字/布尔值/everything...