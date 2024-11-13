class A:
    a = 1
    num = 9
    def c(self):
        print("A类中的c方法被调用")

class B():
    i = 666
    num = 8
    def c(self):
        print("B类中的c方法被调用")

class C(A, B): # 如果子类需要继承多个父类，可以在括号中进行添加
    pass

# 多继承的时候父类的属性和方法不重名调用不受影响
c1 = C()
# 如果重名那么会使用？父类方法或者属性
# 优先使用先继承的父类的属性或者方法
print(c1.num) # 9 C(A, B)
print(c1.num) # 8 C(B, A)
c1.c() # C(A, B) -> A类中的c方法被调用
c1.c() # C(B, A) -> B类中的c方法被调用
# 继承顺序，可以使用mro魔法属性获取继承关系
# 注意：获取继承关系是通过类.__mro__ 魔法属性进行获取
# <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>
print(C.__mro__)
# 通过类调用mro()方法也是可以获得的
print(C.mro())