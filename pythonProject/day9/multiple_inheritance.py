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


class B():
   i = 666
   def f(self):
       print("B类中的f实例方法被调用")

class C(A, B): # 如果子类需要继承多个父类，可以在括号中进行添加
    pass

c1 = C()
# 使用A类中的类属性，实例属性
print(c1.a)
print(c1.b)
# 使用A类中的c实例方法
c1.c()
# 使用B类中类属性
print(c1.i)
c1.f()