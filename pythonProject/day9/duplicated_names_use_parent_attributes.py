class A:
    def __init__(self):
        self.a = 1
        print(f"父类的init没有调用之后 self.a: {self.a}")

class B(A):
    # 当父类和子类有相同的属性或者方法，优先使用子类，不会调用父类
    def __init__(self):
        self.a = 3
        print(f"父类的init没有调用之前 self.a: {self.a}")
        super().__init__() # 通过调用父类魔法函数覆盖掉a的值

b1 = B()
# 父类中和子类中的实例属性重名的时候，
# 如果手动调用父类的init获取实例属性跟子类重名的会覆盖值
print(b1.a) # 1