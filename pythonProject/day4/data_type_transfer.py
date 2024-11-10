# # 字符串类型转化为整数类型
# # 前提：字符串的元素为整数才能进行
# str1 = "188"
# print(str1)
# print(type(str1))
# # 字符串在控制台输出的时候默认会去掉引号
# name = "天秋"
# print(name)
#
# # 通过内建函数int()转化为整数类型
# int1 = int(str1)
# print(int1)
# print(type(int1))
#
# # 因为字符串里元素不是整数, 所以无法转化为整数
# name2 = int(name)
# print(name2)
# print(type(name2))

# 获取用户输入的内容: input()
# 默认所有获取的内容都当作字符串处理.
# num1 = input("请输入一个整数或者小数：")
# print(num1)
# print(type(num1))
# # 转换为整数类型之后的值
# num1 = int(num1)
# print(num1)
# print(type(num1))
# # 转换为浮点数类型之后的值
# num1 = float(num1)
# print(num1)
# print(type(num1))

# list1 = "[1, 2, 3]"
# print(list1)
# print(type(list1))
# list1 = list(list1)

# i = input("请输入Python中常用的数据类型：") # '[1, 2, 3]'
# print(i)
# print(type(i))
# # 使用eval内建函数将字符串元素值转化为python中对应的数据类型
# # eval函数的功能特别强大 => 把字符串去掉 将输入转化为相应的数据类型
# i = eval(i)
# print(i) # [1, 2, 3]
# print(type(i))

# list1 = [1,2,3,2,3,3,3,3,6, 5, 8, 9, 65, 3, 212, 2,1, 35, 6]
# # 列表转化为元组
# print(list1) # [1, 2, 3, 2, 3, 3, 3, 3, 6, 5, 8, 9, 65, 3, 212, 2, 1, 35, 6]
# print(type(list1)) # <class 'list'>
# print("-" * 100)
# list1 = tuple(list1)
# print(list1) # (1, 2, 3, 2, 3, 3, 3, 3, 6, 5, 8, 9, 65, 3, 212, 2, 1, 35, 6)
# print(type(list1)) # <class 'tuple'>
# print("-" * 100)
# list1 = list(list1)
# print(list1) # [1, 2, 3, 2, 3, 3, 3, 3, 6, 5, 8, 9, 65, 3, 212, 2, 1, 35, 6]
# print(type(list1)) # <class 'list'>

# # 将列表转集合 => 去重
# list1 = set(list1)
# print(list1) # {1, 2, 3, 65, 5, 6, 35, 8, 9, 212}
# print(type(list1)) # <class 'set'>
# print("-" * 100)
# list1 = list(list1)
# print(list1) # [1, 2, 3, 65, 5, 6, 35, 8, 9, 212]
# print(type(list1)) # <class 'list'>
# list1 = [1,2,3,2,3,3,3,3,6, 5, 8, 9, 65, 3, 212, 2,1, 35, 6]
# # print(list1) # [1, 2, 3, 2, 3, 3, 3, 3, 6, 5, 8, 9, 65, 3, 212, 2, 1, 35, 6]
# # print(type(list1)) # <class 'list'>
# # 简写
# list1 = list(set(list1))
# print(list1)
# print(type(list1))

t1 = (1, 2, 3, 3,3,3,3,4,5,6,7)
t1 = tuple(set(t1))
print(t1)