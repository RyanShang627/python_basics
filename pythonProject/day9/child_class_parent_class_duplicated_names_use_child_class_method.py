class A:
    num = 9
    def c(self):
        print("A类中的c方法被调用")

class B():
    i = 666
    def f(self):
        print("B类中的f方法被调用")

class C(A, B): # 如果子类需要继承多个父类，可以在括号中进行添加
    num = 1
    def c(self):
        print("C类中的c方法")

c1 = C()
print(c1.num)
c1.c()