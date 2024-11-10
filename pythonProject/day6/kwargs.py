def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

# 不传递关键字参数
func()
# 传递关键字参数
func(a=1,b=2, c=3,name="多多", age=18) # {'a': 1, 'b': 2, 'c': 3, 'name': '多多', 'age': 18}

# 一个函数可以接收任意参数：不定长位置参数结合不定长关键字
def func2(*args, **kwargs):
    print(args)
    print(kwargs)

func2()
func2(1, 2, 3, 4, a=5, b=6)