class A:
    a = 1
    def __init__(self):
        self.b = 2
    def c(self):
        print("A类中的c方法被调用")
    @classmethod
    def d(cls):
        print("A类中的d类方法被调用")
    @staticmethod
    def e():
        print("A类中的e静态方法被调用")

class B(A): # B(继承的类名)
    pass

b1 = B()
print(b1.a)
print(b1.b)
b1.c()
b1.d()
b1.e()