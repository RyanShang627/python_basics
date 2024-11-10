# 函数的引用和传递
def add(num1, num2):
    return num1 + num2

# 函数的引用就是函数的名字: add
# 函数的调用需要使用函数的名字()
# 只使用函数名是不会调用函数
i = add
print(i(3, 5)) # 8
print(type(i)) # <class 'function'>