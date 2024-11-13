# 多态是在继承的基础上才有的具体的表现
class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Miao")

class Dog(Animal):
    def speak(self):
        print("Whaf")

# 定义一个函数调用不同的对象, speak()方法
def animal_speak(animal):
    # 当对象不一样的时候调用的方法也不一样
    animal.speak()

# 创建狗和猫对象
dog = Dog()
cat = Cat()
animal_speak(dog) # Whaf
animal_speak(cat) # Miao
