class A:
    num = 9
    def c(self):
        print("A类中的c方法被调用")


class C(A): # 如果子类需要继承多个父类，可以在括号中进行添加
    num = 1
    def c(self):
        # print("C类中的c方法")
        # 在子类的c实例方法中调用父类的c实例方法
        super().c()

    def c_(self):
        super().c()

    def num_(self):
        print(super().num)

c1 = C()
print(c1.num)
c1.c() # A类中的c方法被调用
c1.num_()