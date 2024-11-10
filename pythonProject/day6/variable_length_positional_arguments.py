def func(*args):
    print(args) # ()
    print(type(args)) # <class 'tuple'>

func()
func(1) # (1,)
func(1, 2, 3, 4, 5, 6) # (1, 2, 3, 4, 5, 6)

def func1(a, b, *args):
    print(args)
    print(type(args))

# 可以接收2到无数个实参
func1(3, 6)