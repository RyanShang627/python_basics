# import model
#
# # 使用变量
# print(model.num)
# # 调用函数
# model.func()

# 注意：如果使用从模块中导入单个函数或者方法，那么其他没有被导入的该模块方法和函数就不能被使用
# 另一种方式调用
# from model import func, func2
# func2(66, 88, "*")
# func()

# 第一种：从包中导入具体的模块：包名.模块名
import ryans.a
ryans.a.func_a()

# 第二种：从包中导入具体的模块：使用from包名import模块名
# 导入包中的模块进行使用
# 注意：包里面无法使用*号导入所有的模块
from ryans import a, b, c
a.func_a()
b.func_b()
c.func_c()