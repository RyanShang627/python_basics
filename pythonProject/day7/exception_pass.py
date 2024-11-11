# 异常的传递
def func1():
    print("func1")
    print(a)

def func2():
    print("func2")
    func3()

def func3():
    print("func3")
    func4()

def func4():
    print("func4")
    func1()

# 函数之间可以相互调用
# 只要调用func2就可以
func2()

