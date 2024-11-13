# 定义匿名函数使用lambda关键字
print((lambda x, y: x + y)(11, 22)) # 33

# 将匿名函数的引用进行传递，然后调用
func1 = lambda x, y: x + y
print(type(func1)) # <class 'function'>
print(func1(6, 8)) # 14