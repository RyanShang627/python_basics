def func(x, y, z):
    print(f"x: {x}, y: {y}, z: {z}")

# 位置参数传递实参
func(1, 2, 3)
# 关键字参数传递实参(关键字：形参名字)
func(z=6, x=8, y=4)
func(6, x=8, y=4) # 注意：位置参数可以结合关键字参数使用，但是不能重复传递实参
# func(z=8, y=4, 6) # 注意：位置参数必须放在关键字参数的前面
# func(1, y=4, z=8) # 这个写法是可行的
# 通过位置参数和关键字参数结合使用的时候，形参和实参数量保持一致
