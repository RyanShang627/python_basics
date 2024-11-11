num = 666

def func():
    print("我是model模块中的func函数")
    print("我被调用啦")
    print("我运行结束啦")

# 定义一个函数完成计算器的功能
# 要求定义3个形参接收3个实参：2个整数和运算符号
# 在函数中进行判断传递的实参符号，输出对应的值
def func2(x, y, z):
    if z == "+":
        print(f"x + y = {x + y}")
    elif z == "-":
        print(f"x - y = {x - y}")
    elif z == "*":
        print(f"x * y = {x * y}")
    elif z == "/":
        if y == 0:
            print("0不能当作被除数")
        else:
            print(f"x / y = {x // y}")

# func2(1, 2, "*")
# func2(4, 2, "+")
# func2(3, 5, "-")