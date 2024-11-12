class Hero:
    def __init__(self):
        # 在类中封装实例属性
        # 名字
        self.name = "百里守约"
        # 生命值
        self.hp = 800
        # 魔法值
        self.mp = 500
    def attack(self):
        print("英雄发起普通攻击")

    def move(self):
        print("执行移动英雄操作")

    def back_city(self):
        print("执行英雄回城操作")

hero1 = Hero()
hero1.move()


# 定义类：使用class关键字类名:
# 类名需要符合标识符的命名规则, 一般类名建议使用大驼峰命名法
class Hero:
   # 在类中定义实例属性需要使用魔法方法: __init__构造方法
   # 魔法方法：以双下划线开头和结尾，而且在特殊情况下自动调用执行
   # init魔法方法会在对象被创建的时候自动执行，也称为构造方法
   # 类当中的函数叫做方法
   # self代表通过类创建出来的对象
   def __init__(self):
       # 在类中封装实例属性
       # 名字
       self.name = "百里守约"
       # 生命值
       self.hp = 800
       # 魔法值
       self.mp = 500


   # 行为和操作封装成实例方法
   # 在类中定义的函数叫做方法
   # 方法和函数的区别：实例方法一定有一个固定的参数self, 代表对象本身
   def attack(self):
       print("英雄发起普通攻击")


   def move(self):
       print("执行移动英雄操作")


   def back_city(self):
       print("执行英雄回城操作")



