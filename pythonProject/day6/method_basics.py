# 拜佛: 初一，十五，以及三十一进行拜佛
# 函数被定义的时候不会被执行
# 函数只有被调用的时候才会执行
def fo_zu():
    print("拜佛！")

while True:
    day = eval(input("请输入今天的日期： "))
    if day == 1:
        fo_zu()
    elif day == 15:
        fo_zu()
    elif day == 31:
        fo_zu()
    elif day == 0:
        break
    else:
        print("今天不是拜佛的日期")


