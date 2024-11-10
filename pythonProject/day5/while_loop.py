import random
list1 = []
# 使用循环体执行重复代码
i = 1 # 循环计数变量
while i < 11:
    # 需要重复执行的代码
    list1.append(random.randint(1, 5))
    # 将循环计数变量持续累加
    i += 1
print(list1)