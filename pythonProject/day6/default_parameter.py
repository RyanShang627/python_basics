def func(x=666, y=111, z=222):
    print(f"x: {x}, y: {y}, z: {z}")

# 当调用函数的时候传递了实参，那么会覆盖默认形参值
func(1, 2, 3) # x: 1, y: 2, z: 3

# 不传递实参，就使用默认形参值
func() # x: 666, y: 111, z: 222

# 当函数有默认值当时候，可以传递实参，也可以不传递
func(1)
func(1, 2)
func(1, 2, 3)

# 使用默认参数可以控制函数的接收实参的范围，可以结合位置参数一起使用
# 形参： 2个位置参数，3个默认参数
def func2(a, b, c=1, d=2, e=3):
    pass
