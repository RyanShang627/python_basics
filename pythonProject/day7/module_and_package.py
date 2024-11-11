# 使用系统自带模块
# 导入的第一种方式
# import random
# # 快捷键导入：alt + enter
# # 使用格式：通过模块名.方法名(实参, 实参...)
# num = random.randint(1, 3)
# print(num)
# import random
# 导入的第二种方式
# from random import randint
# 导入所有的方法
# from random import *
# 从模块中导入具体的方法，可以单个可以多个，也可以所有
# 使用：直接调用 方法名(实参, 实参...)
# num = randint(1, 3)
# print(num)

# 给模块取别名
import random as rd
num = rd.randint(1, 2)
print(num)