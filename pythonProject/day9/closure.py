def func_out(num1):
    def func_inner(num2):
        result = num1 + num2
        print(f"外部函数的num1:{num1}, 内部函数的num2: {num2}, 相加的结果: {result}")
    return func_inner # 外部函数返回内部函数的引用

# 函数只有调用的时候才会执行，定义的时候不会执行
f = func_out(6) # f = func_inner 外部函数的num1:6, 内部函数的num2: 8, 相加的结果: 14
f(8) # f(8) = func_inner(8)

# 简写
func_out(1)(2) # 外部函数的num1:1, 内部函数的num2: 2, 相加的结果: 3